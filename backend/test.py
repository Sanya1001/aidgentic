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

  with open(r'./data/notifications.jsonl', 'a', newline='') as f:
    # update json file.

    # fieldnames = ['ngo_id', 'timestamp', 'report']

    for ngo_id in ngo_ids:
      new_row = {
        "ngo_id": ngo_id,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'report': 'report'
      }
      
      # add new row to jsonl file
      
      f.write(json.dumps(new_row) + '\n')

      #   {
      #     'ngo_id': ngo_id,
      #     'report': report,
      #     'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      # }))


if __name__ == '__main__':
  asyncio.run(test())
