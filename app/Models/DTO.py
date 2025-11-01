from pydantic import BaseModel, EmailStr

# Data model for user signup --
class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str

# Data model for user login --
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Response model for auth
class AuthResponse(BaseModel):
    id: str
    token: str