# Backend

Base repository for the backend API of `OCRed`.

## Running locally
1. Create a virtual environment
```
python -m venv .venv
```
2. Activate the environment
```
.venv/Scripts/activate
```
3. Install the dependencies
```
python -m pip install -r requirements.txt
```
4. Change directory and start the server
```
cd backend
uvicorn main:app --reload
```