from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import re


emotion_model_name = "Jinuuuu/KoELECTRA_fine_tunning_emotion"
cause_model_name = "Jinuuuu/KoELECTRA_fine_tunning_emotion"

tokenizer = AutoTokenizer.from_pretrained(emotion_model_name)
emotion_model = AutoModelForSequenceClassification.from_pretrained(emotion_model_name)
cause_model = AutoModelForSequenceClassification.from_pretrained(cause_model_name)


emotion_labels = ['행복(Happiness)', '슬픔(Sadness)', '분노(Anger)', '공포(Fear)', '놀람(Surprise)', '혐오(Disgust)']

cause_labels = [
    "대인관계 요인", "자기개념 및 자존감", "트라우마 및 생애사적 사건",
    "스트레스 및 환경적 요인", "생물학적 및 신체적 요인",
    "인지적 왜곡 및 기대 불일치", "도덕적 판단 및 가치 갈등",
    "실존적 요인", "사회문화적 요인", "정체성 관련 요인"
]

THRESHOLD = 0.5


def preprocess(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(.)\1{4,}', r'\1\1\1', text)
    text = re.sub(r'(https?://|www\.)\S+', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'\S+@\S+\.\S+', '', text)
    return text

def analyze_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():
        outputs = emotion_model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    return {label: float(probs[0][i]) for i, label in enumerate(emotion_labels)}

def analyze_causes(text, top_n=2):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():
        outputs = cause_model(**inputs)
    probs = torch.sigmoid(outputs.logits)
    top_indices = torch.topk(probs[0], top_n).indices.tolist()
    return [(cause_labels[i], float(probs[0][i])) for i in top_indices]


text = "아직 월급이 안들어왔어서 너무 슬퍼. 친구들이랑 약속도 못잡겠고, 요즘은 그냥 아무것도 하기 싫어. 일도 하기 싫고, 그냥 누워만 있고 싶어."
cleaned_text = preprocess(text)


emotion_result = analyze_emotion(cleaned_text)
top_emotion = max(emotion_result.items(), key=lambda x: x[1])


cause_result = analyze_causes(cleaned_text)


print("✅ 감정 분석 결과:")
if top_emotion[1] > THRESHOLD:
    print(f"{top_emotion[0]}: {top_emotion[1]:.3f}")
else:
    print("분석 실패")

print("\n✅ 감정 원인 예측:")
if any(prob > THRESHOLD for _, prob in cause_result):
    for label, prob in cause_result:
        print(f"{label}: {prob:.3f}")
else:
    for label, prob in cause_result:
        print("분석 실패")
        print(f"{label}: {prob:.3f}")
