import requests
import asyncio
import json
import datetime


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

  with open('./data/notifications.csv', 'w') as f:
    # update json file.
    # add new document for each ngo_id and report
    for ngo_id in ngo_ids:
      f.write(','.join
        
        
      #   {
      #     'ngo_id': ngo_id,
      #     'report': report,
      #     'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      # }))


if __name__ == '__main__':
  asyncio.run(test())
