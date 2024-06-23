import requests
import asyncio

async def test():

  # test post
  result = requests.post('http://localhost:8000/invoke')

  print(result.json())

if __name__ == '__main__':
  asyncio.run(test())




