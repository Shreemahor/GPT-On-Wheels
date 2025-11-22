# alternative to Openrouter using local llm - it just another option

from langchain_ollama import ChatOllama

from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
import os
_dotenv_path = find_dotenv(usecwd=True)
if _dotenv_path:
    load_dotenv(_dotenv_path)
your_base_url = os.getenv("BASE_URL")

# local equivalent of llm from Openrouter
# the base_url parameter is only for the server option
ollama_agent = ChatOllama(model="gemma3:4b", base_url=your_base_url)

# testing ollama agent
# print(ollama_agent.invoke("hello").content)

import base64
from langchain_core.messages.human import HumanMessage

# openening image
with open("frog.jpg", "rb") as image_file:
    image_bytes = image_file.read()
    base64_bytes = base64.b64encode(image_bytes).decode("utf-8") # preparing image

prompt = [{"type": "text", "text":"Describe this image and its theme in detail:"},  # prompt 
          {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_bytes}"}}]

response = ollama_agent.invoke([HumanMessage(content=prompt)]) 
print(response.content) # description of the image

# you could integrate this into MCP_agent.py and use this in place of the llm from Openrouter
# this file is just a backup and second option if Openrouter is down or not working
