"""This file enables the AI to see what is going on around it using the camera and describe it using the llm
There is a loop that asks the user if they want to make the aI look again"""

# importing necessary libraries
from agent import llm, agent
from langchain_core.messages.human import HumanMessage
from picamera2 import Picamera2, Preview
from time import sleep
import asyncio
from agent import viewer

log = ""
while True:
    if input("Do you want to run the test? (y/n): ").lower() != "y":  # checking for user input
        print(log)
        break
    cam = Picamera2()
    try:
        camera_config = cam.create_still_configuration(main={"size": (1920, 1080)}) # creating camera configuration
        cam.configure(camera_config)
        cam.start()
        sleep(2)
        cam.capture_file("/home/shreemahor5/Python/Artificial-Intelligence/image.jpg")
    finally:
        cam.stop()
        cam.close()  
    
    answer = asyncio.run(viewer()) # running viewer
    print(answer) # printing description
    log = log + "\n" + answer # printing full log of descriptions
