import os
from datetime import date
from views import Index, About, NotFound404, Contacts, Calendar, Direction


# front controller
def secret_front(request):
    request['data'] = date.today()
    request['user_name'] = os.getlogin()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/direction/': Direction(),
    '/calendar/': Calendar(),
    '/contacts/': Contacts(),
    '/about/': About(),
    '/page_not_found_404/': NotFound404()
}

