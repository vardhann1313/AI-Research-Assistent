from crewai import Agent, LLM
import os
from app.Agents.agentTools import FetchChatTool, RagTool
from app.Agents.ragChain import get_retriever

def create_agent(chat_id: str):
    """Create a new agent with tools for the given chat_id."""
    # Get llm model
    llm = LLM(
        model="gemini/gemini-2.5-flash", 
        temperature=0.3, 
        api_key=os.getenv('GEMINI_API_KEY')
    )

    # Get retriever for chatId
    retriever = get_retriever(chat_id=chat_id)
    
    # Create agent with tools
    agent = Agent(
        role="Research Assistant",
        goal=f"Help with research and answer questions for chat {chat_id}",
        backstory="You are a helpful AI research assistant.",
        llm=llm,
        verbose=True,
        tools=[
            FetchChatTool(chat_id=chat_id),
            RagTool(retriever=retriever)
        ]
    )
    
    return agent
