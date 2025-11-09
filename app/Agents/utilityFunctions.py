# Inbuilt Imports
from fastapi import HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
# Custom imports
from app.Agents.agent import ask_agent


# Function to generate title for chat
async def generate_chat_title(chat_id: str, question: str) -> str:

    # Prompt for generation title based on uploaded docs
    title_promt = f"""
    Analyze the user question: {question} and generate a concise, descriptive title (5-7 words).
    The Title should be:
    1. Clear and specific
    2. Relevant to what user asked
    Return only the title, nothing else.
    """

    # Try Except for safety
    try:
        output = await ask_agent(chat_id=chat_id, question=title_promt)
        return output.raw.strip('"\'\n') or chat_id

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong while generating title !"
        )

# Function to generate greet message
async def generate_greet_msg(chat_id: str) -> str:

    # Prompt for generating greet message for user
    welcome_prompt = f"""
    Generate a friendly welcome message for user..
    The message should:
    1. Greet the user
    2. Ask how can you help him today
    4. Keep it concise (1-2 sentences max)
    """

    # Try except for safety
    try:
        output = await ask_agent(chat_id=chat_id, question=welcome_prompt)
        return output.raw.strip()

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong while generating greet msg !"
        )


