# Inbuilt module imports
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from fastapi import HTTPException, UploadFile
from bson.objectid import ObjectId 

# Custom module imports 
from app.Agents.agent import ask_agent
from app.Agents.ragChain import process_chat_document
from app.Models.chatModel import ChatSession, Message
from app.Utils.dbUtlis import DB
from app.Utils.jwtUtils import validate_token
from app.Utils.fileUtils import save_file


# New chat function (Working)
async def new_chat_service(token: str, file: UploadFile):

    try:
        # Extract email from token
        email = validate_token(token=token)

        # Upload file in local storage
        result = await save_file(file=file)

        # Create new chat in db
        new_chat = ChatSession(user_email=email, title="Dummy", filepath=result["path"], message=[])
        output = await DB["chats"].insert_one(new_chat.model_dump())

        # Extract filepath & chat Id / chat session Id and send back
        chat_id = str(output.inserted_id)
        filepath = result["path"]

        # Call embedding function to create chunks or doc and save embeddings in vectorDB
        ragOutput = process_chat_document(file_path=filepath, chat_id=chat_id)

        # Create greet msg
        welcomeMsg = Message(role="Assistent", content="Hey, How can i help you ?")

        # Update both in chat
        await DB["chats"].update_one(
            {"_id": ObjectId(chat_id)},
            {
                "$push": {"message": welcomeMsg.model_dump()}
            }
        )

        # Return response
        return JSONResponse(
            status_code=HTTP_202_ACCEPTED,
            content={
                "message": "Context uploaded succesfully !",
                "chunk_len": ragOutput["chunk_len"],
                "success": True,
                "chat_info": {
                    "chat_id": chat_id,
                    "welcomeMsg": "Hey, How can i help you ?"
                }
            }
        )

    # Handle exceptions 
    except HTTPException:
        raise

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong !"
        )

# Answer question function (Not working)
async def ask_model_service(chat_id: str, question: str):
    
    try:
        # Varify chat exists
        chat_doc = await DB["chats"].find_one({"_id": ObjectId(chat_id)})
        if not chat_doc:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="Chat not found !"
            )

        # Ask model with context (Issue in ragChain file with imports)
        answer = await ask_agent(chat_id=chat_id, question=question)

        # Save question and answer in chat
        # Prepare message
        new_message = [Message(role="User", content=question).model_dump(),
                       Message(role="Assistent", content=answer).model_dump()]
        # Save message in chat
        result = await DB["chats"].update_one(
            {"_id": ObjectId(chat_id)},
            {"$push": {"message": {"$each": list(new_message)}}}
        )

        # Check if chat saved
        if not result:
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error while saving chat !"
            )

        # Return answer
        return JSONResponse(
            status_code=HTTP_200_OK,
            content={
                "success": True,
                "answer": answer
            }
        )

    # Handle exception
    except HTTPException:
        raise

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong in ask_model_service !"
        )

