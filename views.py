from bubles_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class About:
    def __call__(self, request):
        return '200 OK', render('about.html', user_name=request.get('user_name', None))


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html')


class Calendar:
    def __call__(self, request):
        return '200 OK', render('calendar.html', data=request.get('data', None))


class Direction:
    def __call__(self, request):
        return '200 OK', render('direction.html')


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', render('page_not_found_404.html')

"""
class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
"""
