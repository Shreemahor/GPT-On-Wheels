# Code

This has all of the software for the current prototype. Everything is in python. In the future, I will add lots more. These inlude but are not limited to Audio recordeing file, Audio playing file, and a Mecahnum wheels file
For now, the 3 main files to run are **autonomous.py, watch.py, interpret.py**. These 3 files represent the 3 functionalities for GPT On Wheels.

#### Autonomous

GPT On Wheels moves around, avoids obstacles and observes the environment. At the end of the run there is a log that says all of what the AI has seen throughout.
<img width="378" height="775" alt="image" src="https://github.com/user-attachments/assets/4eaa7872-897f-4b5c-85fb-e61515b38301" />

#### Watch

GPT On Wheels watches what is in front of it. It will describe what is in the camera.
<img width="1260" height="945" alt="image" src="https://github.com/user-attachments/assets/fb8714c8-93b7-4208-b196-2bdb3f76391f" />

#### Interpret

GPT On Wheels interpets what's in front of it, and decides what to do (go forward or backward). 
Since the AI has to make a decision itself, using interpret requires a more powerful llm that supports tool calling (more in Artificial-Intelligence's README)
![interpret-picture](https://github.com/user-attachments/assets/47fbc6ba-bde4-41ea-a50c-0278128fac58)

## Guide

Code has two subdirectories, - Artificial Intelligence which has most of the logic and Electronics,Sensors,Motors which has testing files for hardware parts.

### Electronics,Sensors,Motors

Has files for hardware, mostly using gpiozero.
  - motors
  - distance sensor
  - obstacle avoidance
  - motor turning

### Artificial-Intelligence

Houses the main logic. There are **autonomous.py, watch.py, and interpret.py** in here. There is also the MCP_agent.py file that actually has most of the logic. Additionally there is the MCP.py for
interpret and api_key.py for testing the api key and test.py for testing logic.

##### Vocab

LLM - large language model like ChatGPT what actually powers the decision making and looking.

MCP - model context protocol how interpret.py gives access to the AI actualy choosing what to do

Langchain - library for using all of this

There are api key setup insturctions in ARtificial-Intelligence's README.
First check the simpler api_key and test then move on to MCP_agent and MCP then the final 3 running files.
