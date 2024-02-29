from django.contrib import admin
from .models import Teacher, Student, Product, Lesson, Group, UserProductAccess


@admin.register(Teacher)
class CategoryTeacher(admin.ModelAdmin):
    list_display = ('id', 'get_full_name')

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    get_full_name.short_description = 'Фамилия и имя'


@admin.register(Student)
class CategoryTeacher(admin.ModelAdmin):
    def get_full_name(self, obj):
        return obj.user.get_full_name()

    get_full_name.short_description = 'Фамилия и имя'


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
        return ", ".join([f'{student.user.first_name} {student.user.last_name}' for student in obj.students.all()])

    get_students_list.short_description = 'Студенты'


@admin.register(UserProductAccess)
class CategoryTeacher(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')