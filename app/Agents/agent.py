from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain

# Custom imports
from app.Agents.ragChain import get_retriever

# Create llm
import os

from app.Agents.tools import get_chat_history
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY"))

# Create ChatPromptTemplate
prompt = ChatPromptTemplate.from_template(
    """
        Answer the following question based on the provided context, last 6 messages and your basic knowledge.
        Think step by step before providing a detailed answer.

        <chat_history>
            {chat_history}
        </chat_history>

        <context>
            Context: {context}
        </context>
        Question: {input}
    """
)

# Create a document chain
document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)

# Function to be used by every function to ask to agent
async def ask_agent(chat_id: str, question: str):

    # Get agent
    retriever = get_retriever(chat_id=chat_id)

    # Create a retrieval chain
    retrieval_chain = create_retrieval_chain(
        retriever=retriever,
        combine_docs_chain=document_chain
    )

    # Create chat history
    chat_history = await get_chat_history(chat_id=chat_id)

    # Invoke retrieval chain
    response = await retrieval_chain.ainvoke({
        "input": question,
        "chat_history": chat_history
    })
    
    return response['answer']


