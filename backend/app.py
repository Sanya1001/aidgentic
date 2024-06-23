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

NOTIFICATION_FILE = r'./data/notifications.json'
SUBMISSIONS_FILE = r'./data/submissions.json'
@app.post('/invoke')
async def invoke():
    with open(SUBMISSIONS_FILE, 'r') as f:
        data = json.load(f)
    print([report['read'] for report in data])
    if all (report['read'] for report in data):
        print('All reports have been read')
        return {'message': 'All reports have been read'}
    with open(NOTIFICATION_FILE, 'w', newline='') as f:
        data = graph.invoke()
        report = data['body']
        title = data['title']

        try:
            current_notifications = json.load(open(NOTIFICATION_FILE, 'r'))
        except json.decoder.JSONDecodeError:
            current_notifications = []
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

    # set all submissions to read
    with open(SUBMISSIONS_FILE, 'r') as f:
        data = json.load(f)
        for report in data:
            report['read'] = True
    with open(SUBMISSIONS_FILE, 'w') as f:
        json.dump(data, f, indent = 2)
    return {'message': 'Reports have been sent to NGOs'}
@app.get('/notifications')  # get all notifications
async def get_notifications():
    try:
        current_notifications = json.load(open(NOTIFICATION_FILE, 'r'))
    except json.decoder.JSONDecodeError:
        current_notifications = []

    return current_notifications