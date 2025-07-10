# EmoBin프로젝트의 서버입니다.   

> **구름톤 유니트 경인지부 해커톤 출전작**
---
## 서비스 한 줄 요약

**프론트로 부터 텍스트를 입력 받아 분석 결과를 저장 및 전달**

---


* **Backend**: Spring Boot
* **Database**: MySQL, Redis
* **AI Integration**: OpenAI
* **DevOps**: GitHub Actions, AWS EC2
  
---
## ERD(초기 버전-수정 가능) 
![EmoBin_BE](https://github.com/user-attachments/assets/693aa782-1ef4-4a04-a88b-f8306ea43514)
 
|  테이블 명 | 설명                |
|---------------------|-------------|
| `members`     | 사용자 정보 (닉네임, 생년월일, 성별, 프로) 저장 |
| `emotion_history`  | 사용자의 결과를 저장     |
| `emotion_causes`    | 검사결과에서 사용되는 감정 원인이 저장      |
| `daily_summary`   | 감정 달력에서 사용하는 해당 당일의 온도 관련 정보 저장         |
| `monthly_summary`   | 감정 달력에서 사용하는 해당 달의 온도 관련 정보 저장         |
