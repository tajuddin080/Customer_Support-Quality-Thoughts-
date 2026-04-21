from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv


load_dotenv()
project = os.getenv("GOOGLE_CLOUD_PROJECT")


model = "gemini-2.5-flash-lite"

def get_llm(model:str):
    
    return (ChatGoogleGenerativeAI(
    model = model,
    vertexai = True,
    project = project
    )
    )