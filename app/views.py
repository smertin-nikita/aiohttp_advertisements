import json

from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    return web.Response(text='Hello Aiohttp!')


@routes.view('/advertisements/{id}')
class Advertisement(web.View):
    async def get(self):
        return web.Response(body=json.dump(id))

    # async def post(self):
    #     return await post_resp(self.request)