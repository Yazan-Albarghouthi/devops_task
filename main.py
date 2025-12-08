from fastapi import FastAPI, HTTPException

app = FastAPI()

def extract_text_field(payload: dict) -> str:
    text = payload.get("text")
    if text is None:
        raise HTTPException(
            status_code=400,
            detail="text field is required in the request body"
        )
    if not isinstance(text, str):
        raise HTTPException(
            status_code=400,
            detail="text field must be a string"
        )
    return text


@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.post("/reverse")
def reverse_text(payload: dict):
    text = extract_text_field(payload)
    reversed_text = text[::-1]
    return {"result": reversed_text}


@app.post("/word-count")
def word_count(payload: dict):
    text = extract_text_field(payload)
    words = text.strip().split()
    count = len(words)
    return {"count": count}


@app.post("/uppercase")
def uppercase(payload: dict):
    text = extract_text_field(payload)
    upper_text = text.upper()
    return {"result": upper_text}
