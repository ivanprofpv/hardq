from rest_framework import serializers

from hardschool.models import Product, Teacher

# Класс указан, так как является ключом Продукта
class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ['user',]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # Указываем, что поле сериализатора будет использоваться через метод get_lessons_in_product
    lessons_in_product = serializers.SerializerMethodField()

    # Запрашиваем количество уроков в продукте через обратную связь
    # (у урока смотрим ключ продукта)
    def get_lessons_in_product(self, product):
        return product.lesson_set.count()

    class Meta:
        model = Product
        fields = ['teacher', 'title', 'start_date_time', 'price',
                  'max_students', 'min_students', 'lessons_in_product']


