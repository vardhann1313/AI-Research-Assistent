from fastapi import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

# Important imports ...
from app.Models.DTO import AuthResponse
from app.Utils.dbUtlis import DB
from app.Utils.jwtUtils import create_token, validate_token
from app.Utils.passwordUtils import hash_password, match_password

# Signup function
async def signupService(user: dict) -> AuthResponse:
    try:
        # Checking if user is already present
        if await DB["users"].find_one({"email": user["email"]}):
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="User already registered !"
            )

        # hash password
        user["password"] = hash_password(user["password"])

        # Store in DB
        result = await DB["users"].insert_one(user)

        # Retrieve Id and Email
        id = str(result.inserted_id)
        email = user["email"]

        # Generate token
        token = create_token(data={"email": email})

        # Send response
        return AuthResponse(id=id, token=token)

    # If HTTP exception, re-raise it
    except HTTPException:
        raise 

    # If other, catch it and raise HTTP exception
    except Exception as e:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong !"
        )

# Login function
async def loginService(user: dict) -> AuthResponse:
    try:
        # Checking if user is present
        found_user = await DB["users"].find_one({"email": user["email"]})

        if not found_user:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="User not found !"
            )

        # match password
        isMatch = match_password(user["password"], found_user["password"])

        # If not matched
        if not isMatch:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Invalid email or password !"
            )

        # Retrieve Id and Email
        id = str(found_user["_id"])
        email = found_user["email"]

        # Generate token
        token = create_token(data={"email": email})

        # Send response
        return AuthResponse(id=id, token=token)

    # If HTTP exception, re-raise it
    except HTTPException:
        raise 

    # If other, catch it and raise HTTP exception
    except Exception:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong !"
        )

