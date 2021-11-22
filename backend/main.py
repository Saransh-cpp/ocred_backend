from fastapi import FastAPI
from pydantic import BaseModel
from aiview_ocr import OCR

app = FastAPI()


class Image(BaseModel):
    image: str


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.post("/ocr-meaningful-text")
async def ocr(image: Image):
    ocr = OCR(
        True,
        "/image.jpg",
        r"D:\Saransh\Softwares\Tesseract-OCR\tesseract.exe"
    )
    text = ocr.ocr_meaningful_text()
    return {"extracted text": text}
