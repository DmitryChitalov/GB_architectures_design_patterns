from time import time
import logging
import config_server_log

server_logger = logging.getLogger('server')

class AddRoute:
    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()


class DebugMethod:
    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        def timeit(method):
            def timed(*args, **kw):
                time_start = time()
                result = method(*args, **kw)
                # te = time()
                # delta = te - ts
                delta = time() - time_start
                print(f'DebugMethod --> {self.name} performed {delta:2.2f} ms')
                server_logger.info(f'DebugMethod --> {self.name} performed {delta:2.2f} ms')
                return result
            return timed
        return timeit(cls)
