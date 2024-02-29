from datetime import datetime

from django.shortcuts import render
from pytz import timezone

from hardschool.models import Student, Group, UserProductAccess, Product


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