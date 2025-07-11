#env 파일을 읽어 환경변수 설정
from dotenv import load_dotenv
import os 
load_dotenv()


from openai import OpenAI
# 환경변수에서 실제 키 값을 가져옴
api_key = os.getenv("OPENAI_API_KEY")

# api_key를 키워드 인자로 전달
client = OpenAI(api_key=api_key)

#응답을 받는 객체 선언
completion = client.chat.completions.create(
    # 모델 이름
    model="gpt-3.5-turbo",
    # 프롬프트 메시지
    messages=[
        {
            "role": "user",
            #진짜 프롬프트 메시지
            "content": "너는 누구야?"
        }
    ]
)
#print(completion)
print(completion.choices[0].message.content)