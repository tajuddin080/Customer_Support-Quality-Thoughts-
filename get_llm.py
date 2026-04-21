from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models.base import BaseChatModel
import os
from dotenv import load_dotenv


load_dotenv()
project = os.getenv("GOOGLE_CLOUD_PROJECT")


def get_llm(model:str)-> BaseChatModel:
    
    return (ChatGoogleGenerativeAI(
    model = model,
    vertexai = True,
    project = project
    )
    )