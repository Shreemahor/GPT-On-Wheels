"""Simple file that uses dotenv and os to check that the api key is set correctly"""
# I used this because I got an api key error, but it turns out it was just a wrong path

from dotenv import load_dotenv, find_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

_dotenv_path = find_dotenv(usecwd=True)
if _dotenv_path:
    load_dotenv(_dotenv_path)
my_key = os.getenv("OPENAI_API_KEY")
print(my_key)
