from fastapi import FastAPI
from pydantic import BaseModel
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

    print('data', data)

    report = data['body']
    title = data['title']

    try:
        current_notifications = json.load(open(r'./data/notifications.json', 'r'))
    except json.decoder.JSONDecodeError:
        current_notifications = []

    with open(r'./data/notifications.json', 'w', newline='') as f:
        # update json file.

        # fieldnames = ['ngo_id', 'timestamp', 'report']
        for ngo in data['ngo_list']:
            new_row = {
                "title": title,
                "ngo_name": ngo['name'],
                'resources': ngo['resources'],
                'timestamp': ngo.get('date', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                'report': report
            }

            current_notifications.append(new_row)

        # add new row to jsonl file

        f.write(json.dumps(current_notifications, indent=2))