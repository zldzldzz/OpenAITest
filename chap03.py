from dotenv import load_dotenv
import os 
load_dotenv()

from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

#Role은 역할이다.
