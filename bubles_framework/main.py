import quopri


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class FrameworkBase:

    """Класс Framework - основа фреймворка"""

    def __init__(self, routes_object, fronts_object):
        self.routes_list = routes_object
        self.fronts_lst = fronts_object

    def __call__(self, environ, start_response):
        # получаем адрес, по которому выполнен переход
        path = environ['PATH_INFO']
        # print(environ)

        # добавление закрывающего слеша
        if not path.endswith('/'):
            path = f'{path}/'

        # находим нужный контроллер
        # отработка паттерна page controller
        if path in self.routes_list:
            view = self.routes_list[path]
        else:
            view = self.routes_list['/page_not_found_404/']
            # view = PageNotFound404()
        request = {}
        # наполняем словарь request элементами
        # этот словарь получат все контроллеры
        # отработка паттерна front controller
        for front in self.fronts_lst:
            front(request)
        # запуск контроллера с передачей объекта request
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

'''
    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
'''