from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello World!"}

@app.get('/ocr')
def ocr():
    return {"message": "OCR"}
