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