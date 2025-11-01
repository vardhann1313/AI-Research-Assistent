import os
from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import JWTError, jwt
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_500_INTERNAL_SERVER_ERROR

# Secret details from env file
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")
EXPIRE_TIME = 30

# Function to create JWT token
def create_token(data: dict) -> str:

    # Set expiration time & encoding data 
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_TIME)
    to_encode = data.copy()
    to_encode.update({"exp": expire})

    # Create token
    token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    # Return it
    return token

# Function to validate JWT token
def validate_token(token: str) -> str:
    try:
        # Extract payload from token
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)

        # Extract data from payload
        email: str = payload.get("email")

        # Check if we got email
        if email is None:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Invalid token !"
            )

        # Return email id is everything is fine
        return email

    # Handle is error occues
    except JWTError:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error while validating JWT !"
        )