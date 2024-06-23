from fastapi import FastAPI
from pydantic import BaseModel
from run import invoke_model
import json
from backend.agents.entry_point import MAGraph
import csv
import datetime
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
graph = MAGraph()


@app.post('/invoke')
async def invoke():
    data = graph.invoke()

    ngo_ids = data['ngo_ids']
    report = data['report']

    with open(r'./data/notifications.jsonl', 'a', newline='') as f:

        for ngo_id in ngo_ids:
            new_row = {
                "ngo_id": ngo_id,
                'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'report': report
            }
        
            f.write(json.dumps(new_row) + '\n')
