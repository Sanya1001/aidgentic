import requests
import asyncio
import json
import datetime
import csv


async def test():
  # test post
  # result = requests.post('http://localhost:8000/invoke')

  # print(result.json())

  ngo_ids = [
    '1',
    '2',
    '3'
  ]

  report = 'This is a report'

  try:
    current_notifications = json.load(open(r'./data/notifications.json', 'r'))
  except json.decoder.JSONDecodeError:
    current_notifications = []

  with open(r'./data/notifications.json', 'w', newline='') as f:
    # update json file.

    # fieldnames = ['ngo_id', 'timestamp', 'report']
    for ngo_id in ngo_ids:
      new_row = {
        "ngo_id": ngo_id,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'report': 'report'
      }

      current_notifications.append(new_row)
      
      # add new row to jsonl file

    f.write(json.dumps(current_notifications, indent=2))

      #   {
      #     'ngo_id': ngo_id,
      #     'report': report,
      #     'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      # }))


if __name__ == '__main__':
  asyncio.run(test())
