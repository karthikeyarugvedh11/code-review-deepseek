from fastapi import FastAPI,Form
import requests
app=FastAPI()
@app.post("/review/")
def code_review(code:str=Form(...)):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "deepseek-coder", "prompt": code, "stream": False}
    )
    result = response.json()
    return {"review": result["response"].strip()}