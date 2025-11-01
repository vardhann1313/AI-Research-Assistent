from passlib.context import CryptContext

# Hashing context
pass_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Method for hashing incoming password
def hash_password(password: str) -> str:
    return pass_context.hash(password)

# Method for matching incoming password
def match_password(plain_pass: str, hash_pass: str) -> bool:
    return pass_context.verify(plain_pass, hash_pass)