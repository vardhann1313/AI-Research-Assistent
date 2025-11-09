from typing import Dict, Optional, Any
import asyncio
from app.Agents.agent_utils import create_agent


# Agent manager for creating one agent for one chat.
class AgentManager:
    _instance = None
    _agents: Dict[str, any] = {}
    _lock = asyncio.Lock()
    MAX_AGENTS = 100

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AgentManager, cls).__new__(cls)
        return cls._instance

    # Async function to get context/chat aware agent from pool
    async def get_agent(self, chat_id: str):
        # Aquire lock
        async with self._lock:

            # If already agent created for chat, return it
            if chat_id in self._agents:
                return self._agents[chat_id]

            # If reached maximun agent creation limit, pop one.
            if len(self._agents) >= self.MAX_AGENTS:
                self._agents.pop(next(iter(self._agents)), None)

            # Create new agent with tools
            agent = create_agent(chat_id=chat_id)
            self._agents[chat_id] = agent

            return agent

# Create single instance
agent_manager = AgentManager()

