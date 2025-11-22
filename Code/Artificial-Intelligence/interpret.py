"""This file is where the AI uses the viewer function to see and then uses MCP to make a decision and move. Its between
autonomous and watch in terms of functionality. IN ORDER TO RUN THIS FILE, CHANGE llm's MODEL IN MCP_agent.py TO A
MORE POWERFUL ONE LIKE GPT-4O OR SIMILAR, AS THE CURRENT MODEL CANNOT HANDLE THE AGENT FUNCTIONALITY"""

# importing necessary libraries
from agent import agent
from langchain_core.messages.human import HumanMessage
from picamera2 import Picamera2, Preview
from time import sleep
import asyncio
from agent import viewer

log = ""
while True:
    if input("Do you want to run the test? (y/n): ").lower() != 'y':  # checking for user input
        print(log)
        break
    cam = Picamera2()
    try:
        camera_config = cam.create_still_configuration(main={"size": (1920, 1080)})
        cam.configure(camera_config)
        cam.start()
        sleep(2)
        cam.capture_file("/home/shreemahor5/Python/Robot/Robot/image.jpg")
    finally:
        cam.stop()
        cam.close()  
    
    answer = asyncio.run(viewer()) # output from viewer
    print(answer) # description of what it sees might be "a wall with a paper that says 'go forward'""
    asyncio.run(agent(answer)) # gives this description to the agent to make a decision
    # by now the car has gone forward, backward, or chose to do nothing
    print("Decision Made")
