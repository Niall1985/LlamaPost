from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(groq_api_key = os.getenv('Groq_Key'), model_name = "llama-3.1-8b-instant")

if __name__ == "__main__":
    response = llm.invoke('What is the role of AI in smart cities?')
    print(response.content)