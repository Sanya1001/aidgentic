from fastapi import FastAPI
from pydantic import BaseModel
from run import invoke_model
import json
from agents.
app = FastAPI()

# @app.post("/submit")
# async def submit(data: dict):

#     return {
#         "message": "Data submitted successfully"
#     }

@app.post('/invoke')
async def invoke():

    print('invoking model')

    # load data
    data = json.load(open('./data/submissions.json', 'r'))

    print(data)
    return 

