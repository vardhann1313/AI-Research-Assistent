# Inbuilt imports
from crewai import Agent, LLM, Crew, Task
import os

# Custom imports
from app.Agents.agentTools import FetchChatTool, RagTool
from app.Agents.ragChain import get_retriever

def get_agent_with_tools(chat_id: str):

    # Get llm model
    llm = LLM(
        model="gemini/gemini-2.5-flash", 
        temperature=0.3, 
        api_key=os.getenv('GEMINI_API_KEY')
    )

    # Get retriever for chatId
    retriever = get_retriever(chat_id=chat_id)

    # Get custom tools for your chat
    rag_tool = RagTool(retriever=retriever)
    chat_tool = FetchChatTool(chat_id=chat_id)    

    # Create agent
    agent = Agent(
        llm=llm,
        role="Research Assistant",
        goal="Answer user questions using tools and your thought also, if any tool gives error tell user about it.",
        backstory="I am an AI assistant that can access vector DB for context provided by user and chat history to answer user questions more accurately. I always try to answer precisely. I use tools when they are required. I take context from chats and rag_tool when needed and answer in my words.",
        tools=[rag_tool, chat_tool],
        verbose=True
    )

    # Return agent
    return agent

async def ask_agent(chat_id: str, question: str):

    # Get agent
    agent = get_agent_with_tools(chat_id=chat_id)

    # Prepare task for agent
    task = Task(
        description=question,
        expected_output="A helpful and accurate answer to the user's question",
        agent=agent,
    )

    # Create crew 
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=False,
    )

    # Run crew
    return await crew.kickoff_async()

