from wsgiref.simple_server import make_server

from bubles_framework.main import FrameworkBase
from urls import routes, fronts

from variables import PORT

application = FrameworkBase(routes, fronts)

with make_server('', PORT, application) as httpd:
    print(f"Запуск на порту {PORT}...")
    httpd.serve_forever()
