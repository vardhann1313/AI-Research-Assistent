# Imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv
import uvicorn
import os

# Load env variables
load_dotenv()

# Router imports
from app.Router.FileUpload import FileRouter
from app.Router.Auth import AuthRouter

# Server object
app = FastAPI(
    title="AI Document Summarizer",
    version="0.1.0",
    description="AI-powered document summarization API with authentication and RAG"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session middleware
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET_KEY")
)

# Root route
@app.get("/")
def root_route():
    return {
        "message": "AI Document Summarizer API is running !"
    }

# Routers
# Auth router
app.include_router(AuthRouter, prefix="/api/v1/auth", tags=["auth"])

# File upload router
app.include_router(FileRouter, prefix="/api/v1/file", tags=["FileUpload"])

# Entry point
if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True
    )
