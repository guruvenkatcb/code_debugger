from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Debugger!"}

@app.get("/predict")
def predict():
    return {"prediction": "This is a sample prediction"}

