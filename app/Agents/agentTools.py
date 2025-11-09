# Inbuilt modules
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
# CrewAI imports
from crewai.tools import BaseTool
# Other utility imports
from bson.objectid import ObjectId
from pydantic import Field
from typing import Any
import json


# RAG tool for agent to fetch relevant info from doc
class RagTool(BaseTool):

    # Name of tool
    name: str = "rag_tool"
    # Description of tool
    description: str = "Retrieve relevant context from vector DB by passing asked question to _run function"
    # Parameter of tool
    retriever: Any = Field(...)

    # Run function to run tool
    async def _run(self, question: str) -> str:
        docs = await self.retriever.ainvoke(question)
        return "\n\n".join(d.page_content for d in docs)


# DB tool for agent to fetch chat history
class FetchChatTool(BaseTool):

    # Name of tool
    name: str = "fetch_chat_tool"
    # Discription of tool
    description: str = "Fetch chat history from MongoDB using chat_id"
    # Parameter to fetch chat
    chat_id: str = Field(...)

    # Run function to run tool
    async def _run(self) -> str:

        # Get fresh DB connection
        from motor.motor_asyncio import AsyncIOMotorClient
        import os

        # Create mongo client using url
        client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
        # Connect to your db
        DB = client["ai-document-summarizer"]

        # Get chat history
        chat_doc = await DB["chats"].find_one(
            {"_id": ObjectId(self.chat_id)},
            {"message": {"$slice": -5}}  # MongoDB $slice operator
        )
        
        # If not found
        if not chat_doc:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Chat not found")

        # If found, return Stringified JSON for LLM
        messages = chat_doc.get("message", [])
        return json.dumps(messages, default=str, ensure_ascii=False, indent=2)

