from dotenv import load_dotenv
from google import genai
from app.models import JobAd
from pydantic import ValidationError

load_dotenv()
client = genai.Client()

def parse_job_ad(text: str) -> JobAd:
    for attempt in range(2):
        try:
            response = client.models.generate_content(model="gemini-3.5-flash-lite", contents=("Extract the job ad data :\n" + text), config={"response_mime_type": "application/json", "response_schema": JobAd})
            ad = JobAd.model_validate_json(response.text)
            return ad
        except ValidationError as e:
            last_error = e
    raise ValueError(f"Gemini returned no valid JobAd after 2 attempts: {last_error}")




ThisAd = """Werkstudent (m/w/d) Softwareentwicklung C++/Python
    TechNova GmbH, Berlin (hybrid, 2 Tage remote)
    Veröffentlicht: 14.10.2026

    Deine Aufgaben:
    - Weiterentwicklung unserer Embedded-Software in C++
    - Schreiben von Testskripten in Python
    - Mitarbeit im agilen Team (Scrum)

    Dein Profil:
    - Studium der Informatik oder Technischen Informatik
    - Gute Kenntnisse in C++, erste Erfahrung mit Python
    - Git und Linux sind dir vertraut
    - Deutsch und Englisch fließend

    Umfang: 16-20 Std./Woche
    Kontakt: jobs@technova.example"""

print(parse_job_ad(ThisAd))

