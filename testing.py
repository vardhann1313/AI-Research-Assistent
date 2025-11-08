from app.Agents.ragChain import process_chat_document, get_retriever
from app.Utils.textUtils import extract_text

from langchain_google_genai import ChatGoogleGenerativeAI

print("=========================================================================================")
print("=========================================================================================")

file= r"D:\Harsh\Codes\GitHub\AI-Research-Assistent\Uploads\db9a19882f7b43edaaca4a5a51349db9.pdf"

# Function to ask questions to model (Not working due to imports issue)
async def ask_model(retriever, question: str):
    try:
        # Get model
        llm = ChatGoogleGenerativeAI(
                model="gemini/gemini-2.5-flash",
                temperature=0.3,
                api_key=os.getenv('GEMINI_API_KEY')
            )

        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff",
            return_source_documents=True
        )

        # Get response
        response = await to_thread(qa_chain.invoke, {"query": question})
        answer = response["result"]

        print("==================================================================================")
        print(response)
        print("==================================================================================")

        # Return answer
        return answer

    # Handle exceptions
    except Exception as e:
        print("==================================================================================")
        print(e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong while asking question to model !"
        )



retriever = get_retriever(chat_id="690d6c50a52586131ba2b454")
input = "What is stipend of Harsh Vardhan in LTIMindtree?"

print("=========================================================================================")
print(retriever.invoke(input=input))
print("=========================================================================================")