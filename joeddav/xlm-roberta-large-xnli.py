from transformers import pipeline
# 사전 라이브러리
#pip install torch transformers protobuf

# Zero-shot 분류 파이프라인 생성
classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

# 테스트할 한국어 문장
text = "여자친구가 날 진심으로 사랑하는지 모르겠어, 자꾸 불안해."

# 후보 카테고리 (개발자가 정한 라벨들)
candidate_labels = ["가족", "일", "미래", "지침", "연애", "위로 필요", "자존감"]

# 분류 실행
result = classifier(
    text,
    candidate_labels,
    hypothesis_template="이 문장은 {}와 관련이 있다."
)

# 결과 출력
print("\n✅ 입력 문장:", text)
print("📊 분류 결과:")
for label, score in zip(result["labels"], result["scores"]):
    print(f"  - {label}: {score:.4f}")
