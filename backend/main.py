import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from aiview_ocr import OCR


app = FastAPI()


@app.get("/")
def home():
    return {"message": "AiView backend. Use the endpoint 'docs' for more information."}


@app.post("/ocr-meaningful-text")
async def ocr_endpoint(image: UploadFile = File(...)):

    with open("image.jpg", "wb+") as f:
        f.write(image.file.read())
        f.close()

    ocr = OCR(False, "image.jpg", r"D:\Saransh\Softwares\Tesseract-OCR\tesseract.exe")
    text = ocr.ocr_meaningful_text()

    return {"extracted text": text, "OCRed file": FileResponse("OCR.png")}
