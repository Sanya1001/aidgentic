from fastapi import FastAPI
from pydantic import BaseModel
from run import invoke
import json


app = FastAPI()


@app.post("/submit")
async def submit(data: dict):

    return {
        "message": "Data submitted successfully"
    }

@app.post('/invoke')
async def invoke():
    print('invoking model')

    return invoke()

