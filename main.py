
from fastapi import FastAPI
from dummy_data import get_dummy_ranking

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CAEwatcher API is running"}

@app.get("/ranking")
def ranking():
    return get_dummy_ranking()
