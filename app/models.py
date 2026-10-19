from datetime import date
from pydantic import BaseModel

class JobAd(BaseModel):
    title: str
    company: str
    posted_at: date | None = None
    employment_type: str
    tasks: list[str]
    skills: list[str]
    location: str
    contacts: list[str] | None = None


