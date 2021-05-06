from datetime import date

from bubles_framework.templator import render
from patterns.сreational_patterns import Engine, Logger
from patterns.structural_patterns import AddRoute, DebugMethod


site = Engine()
logger = Logger('main')

routes={}

@AddRoute(routes=routes, url='/')
class Index:
    @DebugMethod(name='Index')
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.categories)

@AddRoute(routes=routes, url='/about/')
class About:
    @DebugMethod(name='About')
    def __call__(self, request):
        return '200 OK', render('about.html')


@AddRoute(routes=routes, url='/study_programs/')
class StudyPrograms:
    @DebugMethod(name='StudyPrograms')
    def __call__(self, request):
        return '200 OK', render('study-programs.html', data=date.today())


class NotFound404:
    @DebugMethod(name='NotFound404')
    def __call__(self, request):
        return '404 WHAT', render('page_not_found_404.html')


@AddRoute(routes=routes, url='/courses-list/')
class CoursesList:
    @DebugMethod(name='CoursesList')
    def __call__(self, request):
        logger.log('Список курсов')
        try:
            category = site.find_category_by_id(int(request['request_params']['id']))
            return '200 OK', render('course_list.html', objects_list=category.courses, name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


@AddRoute(routes=routes, url='/create-course/')
class CreateCourse:
    category_id = -1

    @DebugMethod(name='CreateCourse')
    def __call__(self, request):
        if request['method'] == 'POST':
            # метод пост
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render('course_list.html', objects_list=category.courses,
                                    name=category.name, id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create_course.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'


@AddRoute(routes=routes, url='/create-category/')
class CreateCategory:
    @DebugMethod(name='CreateCategory')
    def __call__(self, request):

        if request['method'] == 'POST':
            # метод пост
            print(request)
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render('courses.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html', categories=categories)


@AddRoute(routes=routes, url='/category-list/')
class CategoryList:
    @DebugMethod(name='CategoryList')
    def __call__(self, request):
        logger.log('Список категорий')
        return '200 OK', render('category_list.html', objects_list=site.categories)


@AddRoute(routes=routes, url='/copy-course/')
class CopyCourse:
    @DebugMethod(name='CopyCourse')
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', render('course_list.html', objects_list=site.courses)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


@AddRoute(routes=routes, url='/contacts/')
class Contacts:
    @DebugMethod(name='Contacts')
    def __call__(self, request):
        return '200 OK', render('contacts.html')


@AddRoute(routes=routes, url='/calendar/')
class Calendar:
    @DebugMethod(name='Calendar')
    def __call__(self, request):
        return '200 OK', render('calendar.html', data=date.today())


@AddRoute(routes=routes, url='/courses/')
class Courses:
    @DebugMethod(name='Courses')
    def __call__(self, request):
        logger.log('Список категорий курсов')
        # print(site.categories)
        return '200 OK', render('courses.html', objects_list=site.categories)


@AddRoute(routes=routes, url='/direction/')
class Direction:
    @DebugMethod(name='Direction')
    def __call__(self, request):
        return '200 OK', render('direction.html')
