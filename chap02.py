from dotenv import load_dotenv
import os 
load_dotenv()

from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

# api_key를 키워드 인자로 전달
client = OpenAI(api_key=api_key)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "너는 누구야?"
        }
    ],
    #창의력 수치 0~2 사이의 값
    # 0에 가까울수록 보수적이고, 2에 가까울수록 창의적임
    temperature=0  
    max_tokens=10  # 최대 토큰 수
)
print(completion.choices[0].message.content)