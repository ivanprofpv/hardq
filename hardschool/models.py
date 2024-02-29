from datetime import timezone

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


class Teacher(models.Model):
    """
    Модель учителя:
    user: связываем учителя с моделью юзера
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()



class Student(models.Model):
    """
    Модель студента:
    user: связываем студента с моделью юзера
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()


class Product(models.Model):
    """
    Модель продукта:
    teacher: ключ на создателя (учителя) (многие к одному)
    title: наименование продукта
    start_date_time: дата начала продукта
    price: цена продукта
    max_min_students: максимум и минимум студентов в продукте
    """
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date_time = models.DateTimeField()
    price = models.IntegerField()
    max_students = models.PositiveIntegerField(default=10)
    min_students = models.PositiveIntegerField(default=2)

    def __str__(self):
        return self.title


class UserProductAccess(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Lesson(models.Model):
    """
    Модель урока:
    product: ключ на продукт (многие к одному)
    title: наименование урока
    url: строка для ввода ссылки на видео
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Group(models.Model):
    """
    Модель группы:
    students: ключ на студентов (многие ко многим)
    product: ключ на продукт (многие к одному)
    title: наименование группы
    """
    students = models.ManyToManyField(Student)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

