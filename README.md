# Ai-job-tracker

A small Python program that makes job hunting easier: paste a job ad, and it extracts the key data (title, company, skills, …) as structured, validated data. Next it will rate each ad against my own skills to find the best matches.

## Status
**Stage 1 of 3 done: LLM parsing core.**
- Stage 2 (planned): fit score against my skills, SQLite database, REST API (FastAPI)
- Stage 3 (planned): Docker, CI with GitHub Actions, deployment

## Example
Input (excerpt from `tests/ads/00_sample.txt`):
```
Werkstudent (m/w/d) Softwareentwicklung C++/Python
TechNova GmbH, Berlin (hybrid, 2 Tage remote)
Veröffentlicht: 14.10.2026
...
```
Output (`python -m app.parser`):
```json
{
  "title": "Werkstudent (m/w/d) Softwareentwicklung C++/Python",
  "company": "TechNova GmbH",
  "posted_at": "2026-10-14",
  "employment_type": "Werkstudent",
  "tasks": [
    "Weiterentwicklung unserer Embedded-Software in C++",
    "Schreiben von Testskripten in Python",
    "Mitarbeit im agilen Team (Scrum)"
  ],
  "skills": [
    "C++",
    "Python",
    "Git",
    "Linux",
    "Deutsch",
    "Englisch"
  ],
  "location": "Berlin (hybrid, 2 Tage remote)",
  "contacts": [
    "jobs@technova.example"
  ]
}
```

## How it works
1. `parse_job_ad(text)` sends the ad to the **Gemini API** with **structured output**, so the answer must match the `JobAd` schema.
2. **Pydantic** validates the JSON into a `JobAd` object (types, required fields, dates).
3. If validation fails, it **retries once**, then raises a clear error.
4. **pytest** runs the parser on real ads and checks that every extracted skill really appears in the ad text, which catches the LLM inventing skills.

## Setup
```bash
git clone git@github.com:XzolyTFU/Ai-job-tracker.git
cd Ai-job-tracker
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Create a `.env` file in the repo root containing `GEMINI_API_KEY=your-key`, then run:
```bash
python -m app.parser
python -m pytest -v
```
Real job ads stay local (`.gitignore`); only a fictional sample ad is committed.

## Tech
Python · Pydantic · Google Gemini API · pytest · python-dotenv