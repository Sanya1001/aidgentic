import requests
import asyncio

async def test():

  # test post
  requests.post('http://localhost:8000/submt', json={'data': 'test'})


if __name__ == '__main__':
  asyncio.run(test())




