# FastAPI Imports
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from fastapi import HTTPException

# AI Imports
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Other Imports
from asyncio import to_thread
import os

# Custom module importss
from app.Config.directoryConfig import CHROMA_DIR
from app.Utils.textUtils import extract_text

# Embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Function to process uploaded context (Working)
def process_chat_document(file_path: str, chat_id: str):

    try:
        # Extract needed details
        ext = os.path.splitext(file_path)[1].lower()
        text = extract_text(file_path=file_path, ext=ext)

        # If doc is empty
        if not text.strip():
            raise ValueError("No readable text found in document !")


        # Split text into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_text(text)

        # Directory
        persist_dir = os.path.join(CHROMA_DIR, chat_id)

        # Store chunks in a collection which is associated chatId
        vectorStore = Chroma.from_texts(
            chunks,
            embeddings,

            # Also persist in local folder
            persist_directory=persist_dir,
            collection_name=chat_id
        )

        # Return chunk len and collection name
        return {
            "collection": chat_id,
            "chunk_len": len(chunks)
        }

    # Handle error if any
    except ValueError:
        raise

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong while proccessing document !"
        )

# Funtion get retriever according to chat id (Working)
def get_retriever(chat_id: str):

    try:
        # Get persist directory
        persist_dir = os.path.join(CHROMA_DIR, chat_id)

        # Check if dir exists
        if not os.path.exists(persist_dir):
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="No vector DB found !"
            )

        # Get vector DB
        vectorDB = Chroma(
            persist_directory=persist_dir,
            embedding_function=embeddings,
            collection_name=chat_id
        )

        # Return retriever with k=2 to get only top 2 most relevant documents
        return vectorDB.as_retriever(search_kwargs={"k": 2})

    # Handle exceptions
    except HTTPException:
        raise

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong !"
        )


