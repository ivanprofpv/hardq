from datetime import datetime

from django.contrib.auth.models import User
from django.http import Http404

from django.db.models import Count
from django.shortcuts import render
from pytz import timezone
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from hardschool.models import Student, Group, UserProductAccess, Product, Lesson, Teacher
from hardschool.serializers import ProductSerializer, TeacherSerializer, LessonSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт получения списка учителей
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт для получения количества продуктов с количеством уроков
    """
    queryset = Product.objects.all()
    # Упорядочиваем по идентификатору, так как это необходимо для пагинации
    queryset = queryset.order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        # Получаем базовый запрос
        response = super().list(request, *args, **kwargs)
        # Аннотируем строку количества уроков в ответ
        response.data['count_lessons'] = (self.get_queryset()
                                              .annotate(lessons_in_product=Count('lesson'))
                                              .values('lessons_in_product'))
        return response


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self):
        # Получаем идентификатор пользователя из параметров запроса
        # К примеру http://127.0.0.1:8000/lessons/?user_id=1
        user_id = self.request.query_params.get('user_id')

        if user_id:
            # Получаем экземпляр Student на основе указанного идентификатора
            student = Student.objects.get(id=user_id)

            # Получаем все объекты UserProductAccess, связанные с пользователем
            user_product_accesses = UserProductAccess.objects.filter(user=student)

            # Получаем список доступных продуктов
            products = [user_product_access.product for user_product_access in user_product_accesses]

            # Получаем все уроки, связанные с доступными продуктами
            queryset = Lesson.objects.filter(product__in=products)

            return queryset
        else:
            return Lesson.objects.none()

    def list(self, request, *args, **kwargs):
        # Получаем исходник из get_queryset
        queryset = self.filter_queryset(self.get_queryset())
        # Проверяем наличие уроков, не пусто ли там
        if not queryset.exists():
            # Если все таки по id пользователя пусто, возвращаем сообщение:
            return Response({"message": "У этого ученика нет уроков"})
        else:
            # Создаем инстанс сериалайзера и передаем список queryset с полученными уроками
            serializer = self.get_serializer(queryset, many=True)
            # И отправляем данные
            return Response(serializer.data)


def sort_students_to_groups(students, groups, start_date_time):
    """
    Функция сортировки студентов по группам
    :param start_date_time: время старта в продукте
    :param students: студенты
    :param groups: группы
    """
    # Создаем копию списка студентов
    students = list(students)
    # Создаем копию списка групп
    groups = list(groups)

    current_time = datetime.now(timezone('Europe/Moscow')) # Надо сравнивать таймзону, иначе ошибка

    if current_time >= start_date_time:
        print("Сортировку студентов можно выполнять только до указанного времени.")
        return

    for group in groups:
        if students:
            free_places = group.product.max_students - group.students.count()

            # Проверяем, что время начала продукта еще не наступило
            if group.product.start_date_time > current_time:

                # Проверяем, что свободных мест больше или столько же, как указано в мин.мест в продукте
                if free_places >= group.product.min_students:

                    # Добавляем студентов в группу, пока есть свободные места и есть студенты
                    while free_places > 0 and students:
                        student = students.pop(0)  # Берем первого студента из оставшихся

                        # Проверяем доступ студента к продукту
                        if has_access(student, group.product):
                            group.students.add(student) # И добавляем в группу
                            free_places -= 1

        else:
            break  # Все студенты распределены, выходим из цикла


def has_access(student, product):
    """
    Функция проверки доступа студента к продукту
    :param student: студент
    :param product: продукт
    :return: True, если у студента есть доступ к продукту, иначе False
    """
    return UserProductAccess.objects.filter(user=student, product=product).exists()


def group_students(request):
    """
    Функция для вызова функции сортировки
    :param request:
    :return:
    """
    students = Student.objects.all()
    groups = Group.objects.all()
    start_date_time = Product.objects.first().start_date_time

    # Вызываем функцию sort_students_to_groups для сортировки студентов по группам
    sort_students_to_groups(students, groups, start_date_time)

    context = {
        'groups': groups
    }

    return render(request, 'group_students.html', context)