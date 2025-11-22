"""MCP (Model Conxtext Protocol) for the Interpet function
Interpet cannot be usd without this but the other functionalities still can.
As a reminder, in order to use interpret the llm must also be powerful.
"""

from gpiozero import Motor
from time import sleep

# defining pins
ENA = 18  
IN1 = 23  
IN2 = 24  
ENB = 19  
IN3 = 20  
IN4 = 21  

# setting up motors
motor_a = Motor(forward=IN1, backward=IN2, enable=ENA, pwm=True)
motor_b = Motor(forward=IN3, backward=IN4, enable=ENB, pwm=True)

# importing MCP
from mcp.server.fastmcp import FastMCP

# initializing MCP with a name
mcp = FastMCP("Movement")

# test tool I used initially
# @mcp.tool()
# def is_even(number: int) -> bool:
#     return number % 2 == 0

# @mcp.tool() decorator makes the function a tool accessible by MCP agents
@mcp.tool()
def forward():
    print("\nForward\n")
    motor_a.forward(0.5) # goes forward
    sleep(2)
    motor_a.stop()


@mcp.tool()
def backward():
    print("\nBackward\n")
    motor_b.backward(0.5) # goes backward
    sleep(2)
    motor_b.stop()

if __name__ == "__main__":
    mcp.run(transport="stdio") # run this file once before using interpret function
