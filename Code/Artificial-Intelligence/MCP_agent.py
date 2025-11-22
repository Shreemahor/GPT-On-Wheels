"""
CORE AI LOGIC FILE - THIS IS WHAT MAKES THIS PROJECT WORK
THIS IS WHAT MAKES GPT ON WHEELS GPT ON WHEELS AND POSSIBLE

This is the most important code file in the entire project. I built this code myself from scratch
using LangChain, LangGraph, and MCP to create an agent that can control a robot.

The key libraries used in this file are:
langchain-openai
langchain-mcp-adapters
langgraph
python-dotenv
mcp
langchain-core
langchain-google-genai
dotenv

The file loads the OpenAI API key, creates an llm, then:
1. Accesses the MCP and defines agent for Interpret
2. Has the viewer function for Watch and Autonomous
"""

# --------------------------------
# 1. Loading Environment
# --------------------------------

# this just ooads the api key using dotenv
from dotenv import load_dotenv, find_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

_dotenv_path = find_dotenv(usecwd=True)
if _dotenv_path:
    load_dotenv(_dotenv_path)
my_key = os.getenv("OPENAI_API_KEY")

# --------------------------------
# 2. Defining LLM
# --------------------------------

# llm that is used for viewer
llm = ChatOpenAI(
    model="meta-llama/llama-4-scout:free", # this is only temporary and it will not work for agent function, for that it requires a more
    # high end lm. But I ran out of free credits, so this is here for now, bu in order for full functionality, change to a more powerful model like gpt-4o or similar
    api_key=my_key, # api key
    base_url="https://openrouter.ai/api/v1", # default base url for openrouter
)

# uncomment to test it
#answer = llm.invoke("Hello").content

# --------------------------------
# 3. Accessing MCP
# --------------------------------

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import base64
from langchain_core.messages.human import HumanMessage
from PIL import Image
# importing everything essential

server_params = StdioServerParameters(
    command="/home/shreemahor5/Python/Code/.venv/bin/python", # .env path
    args=["/home/shreemahor5/Python/Code/Artificial-Intelligence/MCP.py"] # path to MCP code
)

print("going to MCP")

# --------------------------------
# 4. Defining agent - the Interpret function
# --------------------------------

async def agent(description): # accepts the AI description from viewer as parameter
    async with stdio_client(server_params) as (read, write): # initialize stdio client (just necessary for MCP)
        async with ClientSession(read, write) as session: # initialize MCP session
            await session.initialize() # gets the MCP.py running
            tools = await load_mcp_tools(session) # gets the functions from MCP.py
            agent = create_react_agent(llm, tools) # connects the llm and tools to create an agent
            response = await agent.ainvoke({"messages": description + # prompt on how to make decisions
                                            "You have access to the following tools: Forward(for when anything about "
                                            "forward motion or combination of forward is implied or mentioned"
                                            "ward is displayed) and Backward(for when anything about "
                                            "backward motion or combination of backward is implied or mentioned)."})
            print("before MCP")
            print(response)
             #      response["messages"][2].content)
            print("after MCP")

# --------------------------------
# 5. Defining viewer - the Watching and Autonomous function
# --------------------------------

async def viewer():
    img = Image.open(r"/home/shreemahor5/Python/Artificial-Intelligence/image.jpg") # the defualt image is upside down
    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM) # flips it
    flipped_img.save(r"/home/shreemahor5/Python/Artificial-Intelligence/image_flipped.jpg") # saves flipped image

    with open(r"/home/shreemahor5/Python/Artificial-Intelligence/image_flipped.jpg", 'rb') as image_file:
        image_bytes = image_file.read()
        base64_bytes = base64.b64encode(image_bytes).decode("utf-8") # preparing image
    prompt = [ # this prompt is currently unused and is simpler and for testing
    {"type": "text", "text": "Describe the image"},
    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_bytes}"}}, 
    ]
    view_prompt = [ # this is the real prompt used
    {"type": "text", "text": "You are a observative helper that records"
    "what is in the ground view of a household in 2-3 sentences. "},
    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_bytes}"}},
    ]
    return llm.invoke([HumanMessage(content=view_prompt)]).content # this is what the the ai sees
