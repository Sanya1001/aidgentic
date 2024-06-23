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

  with open(r'./data/notifications.csv', 'a', newline='') as f:
    # update json file.
    # add new document for each ngo_id and report

    fieldnames = ['ngo_id', 'timestamp', 'resources', 'report']

    for ngo_id in ngo_ids:
      new_row = {
        "ngo_id": ngo_id,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
        'resources': 'resources', 
        'report': 'report'
      }
      
      writer = csv.DictWriter(f, fieldnames=fieldnames)

      writer.writerow(new_row)

      #   {
      #     'ngo_id': ngo_id,
      #     'report': report,
      #     'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      # }))


if __name__ == '__main__':
  asyncio.run(test())
