from typing import List
from aiview_ocr import OCR
from fastapi.params import Query
from fastapi.responses import FileResponse
from fastapi import FastAPI, File, UploadFile


app = FastAPI()


@app.get("/")
def home():
    return {"message": "AiView backend. Use the endpoint 'docs' for more information."}


@app.post("/ocr-meaningful-text")
async def ocr_meaningful_text_endpoint(image: UploadFile = File(...)):

    with open("image.jpg", "wb+") as f:
        f.write(image.file.read())

    # replace the tesseract location with the location in your environment
    # TODO: change the location here when deploying
    ocr = OCR(False, "image.jpg", r"D:\Saransh\Softwares\Tesseract-OCR\tesseract.exe")
    text = ocr.ocr_meaningful_text()

    return {"extracted text": text, "OCRed file": FileResponse("OCR.png")}


@app.post("/ocr-bill")
async def ocr_bill_endpoint(
    languages: List[str] = Query(["en"]), image: UploadFile = File(...)
):

    with open("image.jpg", "wb+") as f:
        f.write(image.file.read())

    ocr = OCR(False, "image.jpg")
    text = ocr.ocr_sparse_text(languages=languages)

    info = ocr.process_extracted_text_from_invoice()

    return {
        "extracted text": text,
        "extracted information": info,
        "OCRed file": FileResponse("OCR.png"),
    }


@app.post("/ocr-sign-board")
async def ocr_sign_board_endpoint(
    languages: List[str] = Query(["en", "hi"]), image: UploadFile = File(...)
):

    with open("image.jpg", "wb+") as f:
        f.write(image.file.read())

    ocr = OCR(False, "image.jpg")
    text = ocr.ocr_sparse_text(languages=languages)

    return {
        "extracted text": text,
        "OCRed file": FileResponse("OCR.png"),
    }
