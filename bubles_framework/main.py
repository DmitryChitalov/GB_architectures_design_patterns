import quopri
import logging
from bubles_framework.request_processor import GetRequests, PostRequests
import config_server_log
from variables import filial, course_dict, html_id_dicts

server_logger = logging.getLogger('server')


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class FrameworkBase:
    """Класс Framework - основа фреймворка"""

    def __init__(self, routes_object, fronts_object):
        self.routes_list = routes_object
        self.fronts_lst = fronts_object

    def __call__(self, environ, start_response):
        # server_logger.debug(environ)
        # получаем адрес, по которому выполнен переход
        path = environ['PATH_INFO']
        server_logger.info(f'{path}')
        # print(environ)

        # добавление закрывающего слеша
        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        # Получаем все данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            request_data = FrameworkBase.decode_value(data)
            # print(f'Нам пришёл post-запрос: {FrameworkBase.decode_value(data)}')
            server_logger.info(f'Нам пришёл post-запрос: {request_data}')
            OutResult(request_data)

        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            # print(f'Нам пришли GET-параметры: {request_params}')
            server_logger.info(f'Нам пришли GET-параметры: {request_params}')
            request_data = request_params
            OutResult(request_data)

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

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data


def OutResult(request_data):
    user_data={}
    if request_data != {}:
        if 'send_feedback' in request_data:
            # запрос из обратной связи
            user_feedback = dict(name='', email='', phone='', feedback='')
            for el in request_data.items():
                if el[1] != '':
                    user_feedback[el[0]] = el[1]
            print(f'user_feedback={user_feedback}')
            server_logger.info(f'Сформирован словарь обратной связи: {user_feedback}')
        elif 'send_registration' in request_data:
            # запрос записи на курсы
            user_data = dict(name='', email='', phone='', user_filial='', member='')
            for el in request_data.items():
                if el[1] != '':
                    user_data[el[0]] = el[1]
            print(f'user_data={user_data}')
            server_logger.info(f'Сформирован словарь запроса на курсы: {user_data}')
    else:
        user_data = {}

    return user_data
