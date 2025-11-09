from crewai import Crew, Task
from app.Agents.agent_utils import create_agent
from app.Agents.agentManager import agent_manager

# Function to be used by every function to ask to agent
async def ask_agent(chat_id: str, question: str):

    # Get agent
    agent = await agent_manager.get_agent(chat_id=chat_id)

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

