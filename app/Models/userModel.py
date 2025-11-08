from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    profile: str = "https://bournemouth.foodbank.org.uk/wp-content/uploads/sites/64/2023/03/506-5067022_sweet-shap-profile-placeholder-hd-png-download.png"

