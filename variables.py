import logging

PORT = 8080
LOGGING_LEVEL = logging.DEBUG
# LOGGING_LEVEL = logging.INFO
ENCODING = 'utf-8'

SQLBD='legocode.sqlite'

# словари соответствия
filial = {
    'ac': 'LegoCode - Академический',
    'yz': 'LegoCode - ЮЗ',
    'ct': 'LegoCode - Центр',
    'na': 'филиал не выбран'
}

# курсы
course_dict = {'r1': 'Робототехника-1',
               'r2': 'Робототехника-2',
               'u1': 'Юные программмисты-1',
               'u2': 'Юные программмисты-2'
               }

html_id_dicts = {'name': 'Имя', 'email': 'e-mail', 'phone': 'телефон', 'feedback': 'текст сообщения', 'course': 'курс'
    , 'location': 'филиал', 'member': 'уже наш клиент'}

logo='lego_model.png'

COURSE_CATEGORIE={1:'Конструирование', 2:'Робототехника', 3:'Электроиника', 4:'Программирование'}