from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File
from starlette.status import HTTP_400_BAD_REQUEST
from app.Service.chatService import new_chat_service ,ask_model_service

# HTTPBearer for token extraction
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
bearer_scheme = HTTPBearer()

# Router
ChatRouter = APIRouter()

# Router to create new chat
@ChatRouter.post("/new_chat")
async def new_chat(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), file: UploadFile = File(...)):

    # Extract user email from token
    token = credentials.credentials

    # Call service method
    return await new_chat_service(token=token, file=file)
    
# Route to ask questions
@ChatRouter.get("/ask/{chat_id}")
async def ask(
        chat_id: str,
        credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
        question: str = Query(...)
    ):
    
    # Extract token
    token = credentials.credentials

    # Validation
    question = question.strip()
    if not question:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Question can not be empty !"
        )

    # Call service method
    return await ask_model_service(chat_id=chat_id, question=question)

