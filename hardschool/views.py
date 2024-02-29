from django.http import HttpResponse
from django.db import transaction

from hardschool.models import Student, Product, Group


@transaction.atomic
def distribute_students_to_groups():
    # Получаем список всех групп
    groups = Group.objects.all()

    # Получаем список всех продуктов
    products = Product.objects.all()

    return groups, products

    # for product in products:
    #     # Получаем список групп для текущего продукта
    #     product_groups = groups.filter(product=product).order_by('students__count')
    #
    #     # Распределение студентов по группам
    #     students = Student.objects.all()
    #     num_students = students.count()
    #
    #     # Проверка, достаточно ли студентов для формирования групп
    #     if num_students >= product.min_students:
    #         # Распределяем студентов по группам
    #         num_groups = product_groups.count()
    #         min_students_per_group = product.min_students
    #         max_students_per_group = product.max_students
    #
    #         # Вычисляем количество студентов в каждой группе
    #         if num_students <= max_students_per_group * num_groups:
    #             students_per_group = num_students // num_groups
    #             remainder = num_students % num_groups
    #         else:
    #             students_per_group = max_students_per_group
    #             remainder = num_students - max_students_per_group * num_groups
    #
    #         for i, group in enumerate(product_groups):
    #             if i < remainder:
    #                 group.students.set(students[:students_per_group + 1])
    #                 students = students[students_per_group + 1:]
    #             else:
    #                 group.students.set(students[:students_per_group])
    #                 students = students[students_per_group:]
    #
    # # Сохраняем изменения в базе данных
    # groups.save()
    #
    # return groups

def index(request):
    groups = Group.objects.all()

    # Получаем список всех продуктов
    products = Product.objects.all()

    for group in groups:
        print(group)

    for product in products:
        print(product)
    # Возвращение ответа представления
    return groups, products
