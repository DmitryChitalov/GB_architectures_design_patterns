from datetime import date
from views import Index, About, StudyPrograms, CoursesList, CreateCourse, CreateCategory, CategoryList, CopyCourse, \
    Direction, Calendar, Contacts, NotFound404, Courses


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

"""
routes = {
    '/': Index(),
    '/about/': About(),
    #'/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    #'/category-list/': CategoryList(),
    '/copy-course/': CopyCourse(),
    '/direction/': Direction(),
    '/calendar/': Calendar(),
    '/contacts/': Contacts(),
    '/courses/': Courses(),
    '/page_not_found_404/': NotFound404()
}
"""