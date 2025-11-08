import os
from fastapi import APIRouter, HTTPException, Request
from authlib.integrations.starlette_client import OAuth
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

# Custom imports
from app.Models.userModel import User
from app.Models.DTO import AuthResponse, UserLogin, UserSignup
from app.Service.authService import loginService, signupService
from app.Utils.dbUtlis import DB
from app.Utils.jwtUtils import create_token

# Router object
AuthRouter = APIRouter()

# Routes

# Check router
@AuthRouter.get("/check")
def check():
    return {
        "message": "AuthRouter working !"
    }

# Signup router
@AuthRouter.post("/signup")
async def signup(user: UserSignup) -> AuthResponse:
    return await signupService(user.model_dump())

# Login router
@AuthRouter.post("/login")
async def login(user: UserLogin) -> AuthResponse:
    return await loginService(user.model_dump())

# OAuth config and routing 
# OAuth object setup with goolge credentials
oauth = OAuth()
oauth.register(
    name = "google",
    server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration",
    client_id = os.getenv("GOOGLE_CLIENT_ID"),
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET"),
    client_kwargs = {"scope": "openid email profile"},
)

# Continue with google api
@AuthRouter.get("/google")
async def google_oauth(request: Request):
    # Set callback url for google
    redirect_uri = request.url_for("google_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)

# Google callback api
@AuthRouter.get("/google/callback")
async def google_callback(request: Request) -> AuthResponse:
    try:
        # Retrieve goolge token
        google_token = await oauth.google.authorize_access_token(request)

        # Get user_info from google
        user_info = google_token.get("userinfo")

        # If user_info not present, raise exception
        if not user_info:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Failed to fetch user info from google !"
            )

        # Retrieve data from google response
        email = user_info.get("email")
        name = user_info.get("name")
        profile = user_info.get("picture")

        # Check if user already registered
        found_user = await DB["users"].find_one({"email": email})

        # If not, register and get user id
        if not found_user:
            user = User(name=name, email=email, password="", profile=profile)
            result = await DB["users"].insert_one(user.model_dump())
            found_user = user
            found_user["_id"] = str(result.inserted_id)
        else:
            found_user["_id"] = str(found_user["_id"])

        # Retrieve id of user
        id = found_user["_id"]

        # Create token
        token = create_token(data={"email": email})

        # Return response
        return AuthResponse(id=id, token=token)

    # If HTTP exception, raise it again
    except HTTPException:
        raise

    # Global exception
    except Exception:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong !"
        )


