from django.contrib import admin
from .models import Teacher, Student, Product, Lesson, Group


@admin.register(Teacher)
class CategoryTeacher(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Student)
class CategoryTeacher(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Product)
class CategoryTeacher(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'title', 'start_date_time', 'price',
                    'max_students', 'min_students')


@admin.register(Lesson)
class CategoryTeacher(admin.ModelAdmin):
    list_display = ('id', 'product', 'title', 'url')


@admin.register(Group)
class CategoryTeacher(admin.ModelAdmin):
    list_display = ('id', 'get_students_list', 'product', 'title')

    def get_students_list(self, obj):
        return ", ".join([f'{students.first_name} {students.last_name}' for students in obj.students.all()])

    get_students_list.short_description = 'Студенты'