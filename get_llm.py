from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models.base import BaseChatModel
import os
from dotenv import load_dotenv


load_dotenv()
project = os.getenv("GOOGLE_CLOUD_PROJECT")


model = "gemini-2.5-flash-lite"

def get_llm(model:str)-> BaseChatModel:
    
    return (ChatGoogleGenerativeAI(
    model = model,
    vertexai = True,
    project = project
    )
    )