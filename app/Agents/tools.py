# Inbuilt modules
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
# Other utility imports
from bson.objectid import ObjectId
import json
# Custom imports
from app.Utils.dbUtlis import DB

# Function to get chat context from DB
async def get_chat_history(chat_id: str) -> str:

        # Get chat history
        chat_doc = await DB["chats"].find_one(
            {"_id": ObjectId(chat_id)},
            {"message": {"$slice": -6}}  # MongoDB $slice operator
        )
        
        # If not found
        if not chat_doc:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Chat not found")

        # If found, return Stringified JSON for LLM
        messages = chat_doc.get("message", [])
        return json.dumps(messages, default=str, ensure_ascii=False, indent=2)


