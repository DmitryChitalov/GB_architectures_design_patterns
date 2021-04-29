import os
from datetime import date
from views import Index, About, NotFound404, Contacts, Calendar, Direction
from variables import logo


# front controller
def secret_front(request):
    request['data'] = date.today()
    request['user_name'] = os.getlogin()
    path=os.getcwd()
    path.join(f'/templates/res/{logo}')
    request['logo']=f'lego_model.png'
    # request['logo'] = f'{os.getcwd()}/res/{logo}'


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


