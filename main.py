from fastapi import FastAPI
import requests

app = FastAPI()

DEEPSEEK_API_URL = "https://api.deepseek.com/v1/completions"  # Update if needed
DEEPSEEK_API_KEY = "your_api_key_here"  # Replace with your API key

@app.post("/debug/")
async def debug_code(prompt: str):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-coder",  # Choose the correct model (verify with DeepSeek docs)
        "prompt": prompt,
        "max_tokens": 500
    }
    
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get a response from DeepSeek"}

