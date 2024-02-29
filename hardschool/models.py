from django.db import models


class Teacher(models.Model):
    """
    Модель учителя:
    first_name: имя
    last_name: фамилия
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    """
    Модель студента:
    first_name: имя
    last_name: фамилия
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    """
    Модель продукта:
    teacher: ключ на создателя (учителя) (многие к одному)
    title: наименование продукта
    start_date_time: дата начала продукта
    price: цена продукта
    max_students: максимум студентов в продукте
    min_students: минимум студентов в продукте
    """
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date_time = models.DateTimeField()
    price = models.IntegerField()
    max_students = models.IntegerField()
    min_students = models.IntegerField()

    def __str__(self):
        return self.title


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

