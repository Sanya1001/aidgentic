import requests
import time

start_time = time.time()
time_elapsed = 0
# time.sleep(60)
while True:
    print('posting request')
    url = 'http://127.0.0.1:8000/invoke'
    response = requests.post(url)
    print(response)

    time.sleep(30)

# import json
# SUBMISSIONS_FILE = r'./data/submissions.json'
# with open(SUBMISSIONS_FILE, 'r') as f:
#     data = json.load(f)
#     for i, report in enumerate(data):
#         data[i]['read'] = True
#         # save the file
# with open(SUBMISSIONS_FILE, 'w') as f:
#     json.dump(data, f, indent = 2)

# with open(SUBMISSIONS_FILE, 'w') as f:
#     json.dump(data, f, indent = 2)
