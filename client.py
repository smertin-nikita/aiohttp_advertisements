import asyncio
import sys

import aiohttp


HOST = 'http://127.0.0.1:8088'


async def get(path, **kwargs):
    async with aiohttp.client.ClientSession() as client:
        async with client.get(f'{HOST}{path}', **kwargs) as response:
            return await response.text()


async def main():
    result = await get('/advertisements/')
    print(result)

if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(main())
    asyncio.run(main(), debug=True)
