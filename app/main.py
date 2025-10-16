from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.lib.helper import add_numbers

app = FastAPI(title="Simple FastAPI App", version="1.0.0")


class AddRequest(BaseModel):
    a: float
    b: float


@app.get("/")
async def health():
    return {"status": "healthy"}


@app.post("/add")
async def add(req: AddRequest):
    try:
        result = add_numbers(req.a, req.b)
        return {"sum": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
