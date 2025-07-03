from transformers import pipeline
import re

# 1. 감정 및 원인 후보 리스트 (후처리용)
emotion_labels = ["행복", "슬픔", "분노", "놀람", "공포", "혐오"]
cause_labels = [
    "대인관계 요인", "자기개념 및 자존감", "트라우마 및 생애사적 사건",
    "스트레스 및 환경적 요인", "생물학적 및 신체적 요인",
    "인지적 왜곡 및 기대 불일치", "도덕적 판단 및 가치 갈등",
    "실존적 요인", "사회문화적 요인", "정체성 관련 요인"
]

# 2. 모델 로딩
generator = pipeline("text-generation", model="skt/kogpt2-base-v2")

# 3. 사용자 입력 문장
text = "요즘 인간관계도 너무 힘들고 나 자신에 대한 자존감도 낮아졌어요."

# 4. 프롬프트 구성
prompt = f"""
문장을 읽고 감정과 감정의 원인을 추론하세요.

예시 1:
문장: "갑작스럽게 직장을 잃어서 불안하고 우울해요."
감정: 슬픔
감정 원인: 스트레스 및 환경적 요인, 트라우마 및 생애사적 사건

예시 2:
문장: "시험에 떨어져서 무능한 느낌이 들고 화가 나요."
감정: 분노
감정 원인: 자기개념 및 자존감, 인지적 왜곡 및 기대 불일치

예시 3:
문장: "{text}"
감정:
"""

# 5. 생성 실행
output = generator(
    prompt,
    max_new_tokens=100,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

# 6. 생성된 텍스트 가져오기
generated_text = output[0]["generated_text"]

# 7. 감정 및 원인 추출 (정규표현식 기반)
emotion_match = re.search(r"감정:\s*([^\n]+)", generated_text)
cause_match = re.search(r"감정 원인:\s*([^\n]+)", generated_text)

# 8. 결과 파싱
emotion = emotion_match.group(1).strip() if emotion_match else "감정 분석 실패"
causes = cause_match.group(1).strip() if cause_match else "원인 분석 실패"

# 9. 유효성 필터링 (선택: 라벨 안에 있는지 체크)
emotion = emotion if emotion in emotion_labels else "감정 분석 실패"
cause_list = [c.strip() for c in causes.split(",") if c.strip() in cause_labels]

# 10. 최종 출력
print("✅ 감정 분석 결과")
print(f"감정: {emotion}")
print(f"감정 원인: {', '.join(cause_list) if cause_list else '원인 분석 실패'}")
