from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

response = client.models.generate_content(model="gemini-3.5-flash-lite", contents="List the required skills in this job ad :\n" + """Werkstudent (m/w/d) Softwareentwicklung C++/Python
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
Kontakt: jobs@technova.example""")
print(response.text)