import aiohttp

HOST = 'http://127.0.0.1/:8081'


async def get(path, **kwargs):
    async with aiohttp.client.ClientSession() as client:
        async with client.get(f'{HOST}{path}', **kwargs) as response:
            return await response.text()


async def main():
    result = await get('')
    print(result)
