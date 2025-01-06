import os
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import uvicorn
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from httpx._types import ProxyTypes as VerifyTypes


load_dotenv()

app = FastAPI(
    title="Langchain API using FastAPI",
    description="Langchain API using FastAPI and Langserve - Sample application 05-01-2025",
    version="1.0.0",
)

llm=Ollama(model="mistral:latest")

prompt = ChatPromptTemplate.from_template("You are an expert in {topic}. Explain like the User is 5 years old within 150 words")

add_routes(
    app,
    prompt|llm,
    path = "/expert"
    )

if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)