# uv pip install fastapi uvicorn
# uvicorn main:app --host=0.0.0.0 --reload   # 상대방접근허용
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"message": "안녕하세요 KIM HWI 입니다."}
