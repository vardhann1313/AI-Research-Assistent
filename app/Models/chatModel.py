from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# Message format
class Message(BaseModel):
    # Role of message sender
    role: str
    # Content of message
    content: str

    # Timestamp
    timestamp: datetime = Field(default_factory=datetime.utcnow)

# Chat box
class ChatSession(BaseModel):
    # User of chat
    user_email: EmailStr
    # Title of chat
    title: Optional[str] = None
    # Context of chat
    filepath: str
    # Message list
    message: List[Message] = []

    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

