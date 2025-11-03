from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.routing import JSONResponse
from starlette.routing import Router
from starlette.status import HTTP_202_ACCEPTED

from app.Utils.fileUtils import save_file
from app.Utils.jwtUtils import validate_token

# HTTPBearer for token extraction
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
bearer_scheme = HTTPBearer()

# Router
FileRouter = APIRouter()

@FileRouter.post("/upload")
async def upload_file(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), file: UploadFile = File(...)):

    # Extract user email from token
    token = credentials.credentials
    email = validate_token(token=token)

    # Upload file in local storage
    result = await save_file(file=file)

    # Return response
    return JSONResponse(
        status_code=HTTP_202_ACCEPTED,
        content={
            "message": "Context uploaded succesfully !",
            "filename": result["filename"],
            "success": True,
            "result": result
        }
    )

