import asyncio
import sys
from pprint import pprint

import aiohttp


HOST = 'http://127.0.0.1:8088'


async def get(path, **kwargs):
    async with aiohttp.client.ClientSession() as client:
        async with client.get(f'{HOST}{path}', **kwargs) as response:
            return await response.text()


async def post(path, **kwargs):
    async with aiohttp.client.ClientSession() as client:
        async with client.post(f'{HOST}{path}', **kwargs) as response:
            return await response.text()


async def delete(path, **kwargs):
    async with aiohttp.client.ClientSession() as client:
        async with client.delete(f'{HOST}{path}', **kwargs) as response:
            return await response.text()


async def main():
    # result = await post('/advertisements', json={'title': 'Second', 'description': 'First description'})
    # print(result)
    result = await get(f'/advertisements')
    pprint(result)
    result = await delete(f'/advertisements/2')
    print(result)

if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(main())
    asyncio.run(main(), debug=True)
