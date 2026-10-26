# Learning log

## 2026-10-19 · JobAd model (Pydantic)

**Built:** `app/models.py`, a `JobAd` class (Pydantic `BaseModel`) with 8 fields.

### model_validate
- `JobAd.model_validate(d)` returns a `JobAd` object (an instance of the class) when the dict is valid.
- Valid means every required field is present AND every value can be converted to its type.
- Otherwise no object is created and it raises a `ValidationError`. It never returns `False`.
- `model_dump_json()` returns a JSON string (it doesn't write a file). `None` becomes `null`.

### Lax parsing
- An LLM sends text, so numbers and dates can arrive as strings.
- Pydantic converts them to the field's type: `"3"` → `3`, `"2026-10-17"` → `date`.
- JSON has no date type, so dates always arrive as strings.
- Limit: only known formats. `"18.07.2025"` or `"vor 3 Tagen"` fail.
  Fix: ask the LLM for `YYYY-MM-DD`, or write a `field_validator(mode="before")`.

### Design choices
- Required = an ad without it is useless to me: title, company, employment_type, tasks, skills, location.
- `location` is required on purpose. It works as a filter, so ads without it are rejected.

### Mistakes I made
- Named a field `date`, which shadows the imported type (like `int int;` in C). Renamed it to `posted_at`.
- Ran `python` inside `app/` and got `ModuleNotFoundError`. Imports resolve from the folder Python starts in.

## 2026-10-26

**Built:** `app/parser.py` 

### load_dotenv() 

- `load_dotenv()` loads the first .env file it finds (searching upward from the current folder) `"into the environment of the running Python process"` (os.environ), not into the code. 
- It’s gone when the program ends.

### Error Types

- 4xx is mostly a `"client error"` : my request was wrong (bad key, wrong model name, bad request). Exception: 429 means too many requests, so wait and retry. 
- 5xx is a `"server error"`.

### AI Models/ API CALL 

- I switched models because the first one was so crowded that not a single call got through (503 for days). I switched to another model with lighter traffic, which answered my call quickly.

### Parser

- `parse_job_ad` takes a string / plain text (job description) and attempts, with a 2-time for loop, to call the Gemini API, which parses the job ad into **JSON** following the JobAd schema provided in the configuration. 
- If the JSON is validated, parse_job_ad returns the JobAd object (not JSON). If not, it raises a `ValueError` (after 2 failed attempts) that contains the last `ValidationError`.

### Python -m 
- `"python -m app.parser"` searches imports starting from the folder I’m currently in (the repo root), so from app.models import looks for app/ inside the root folder, where it’s found. 
- If python app/parser.py is run, imports are searched from the folder where the script is, so it looks for app/ inside app/, which results in an error.