from aiohttp import web

from app.models import init_pg, close_pg
from app.routes import setup_routes
from app.settings import config

app = web.Application()
setup_routes(app)
app['config'] = config

app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

web.run_app(app, host='127.0.0.1', port=8088)
