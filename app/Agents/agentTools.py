# Inbuilt modules
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from bson.objectid import ObjectId
from pydantic import Field
from typing import Any, List
from crewai.tools import BaseTool


class RagTool(BaseTool):
    name: str = "rag_tool"
    description: str = "Retrieve relevant context from vector DB by passing asked question to _run function"
    retriever: Any = Field(...)

    def _run(self, question: str) -> str:
        docs = self.retriever.invoke(question)
        return "\n\n".join(d.page_content for d in docs)


class FetchChatTool(BaseTool):
    name: str = "fetch_chat_tool"
    description: str = "Fetch chat history from MongoDB using chat_id"
    chat_id: str = Field(...)

    async def _run(self) -> str:

        # Get fresh DB connection
        from motor.motor_asyncio import AsyncIOMotorClient
        import os

        # Create mongo client using url
        client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
        # Connect to your db
        DB = client["ai-document-summarizer"]


        chat_doc = await DB["chats"].find_one(
            {"_id": ObjectId(self.chat_id)},
            {"message": {"$slice": -5}}  # MongoDB $slice operator
        )
        
        if not chat_doc:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Chat not found")

        messages = chat_doc.get("message", [])
        return "\n".join(f"{m['role']}: {m['content']}" for m in messages)


