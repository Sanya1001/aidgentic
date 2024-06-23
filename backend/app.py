from fastapi import FastAPI
from pydantic import BaseModel
from run import invoke_model
import json

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


@app.post('/notify')
async def notify(data: dict):

    ngo_ids = data['ngo_ids']
    report = data['report']

    with open('./data/notifications.json', 'w') as f:
        # update json file. 
        # add new document for each ngo_id and report
        for ngo_id in ngo_ids:
            f.write(json.dumps({
                'ngo_id': ngo_id,
                'report': report
            }))












