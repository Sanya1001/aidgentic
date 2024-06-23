from fastapi import FastAPI
from pydantic import BaseModel
import json
from agents.entry_point import MAGraph
import csv
import datetime
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

# allow all CORS requests
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.get('/notifications')  # get all notifications
async def get_notifications():
    try:
        current_notifications = json.load(open(r'./data/notifications.json', 'r'))
    except json.decoder.JSONDecodeError:
        current_notifications = []

    return current_notifications