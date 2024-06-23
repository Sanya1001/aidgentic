from fastapi import FastAPI
from pydantic import BaseModel
from run import invoke_model
import json
from agents.entry_point import MAGraph
import csv
import datetime
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
graph = MAGraph()


@app.post('/invoke')
async def invoke():
    data = graph.invoke()

    ngo_names = data['ngo_names']
    report = data['report']

    try:
        current_notifications = json.load(open(r'./data/notifications.json', 'r'))
    except json.decoder.JSONDecodeError:
        current_notifications = []

    with open(r'./data/notifications.json', 'w', newline='') as f:
        # update json file.

        # fieldnames = ['ngo_id', 'timestamp', 'report']
        for ngo_id in ngo_names:
            new_row = {
                "ngo_id": ngo_id,
                'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'report': report
            }

        current_notifications.append(new_row)

        # add new row to jsonl file

        f.write(json.dumps(current_notifications, indent=2))