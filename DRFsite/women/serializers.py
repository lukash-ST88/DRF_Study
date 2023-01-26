import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # сериализация текущего пользователя через скрытое поле
    class Meta:
        model = Women
        fields = ('title', 'content', 'cat', 'user')





# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance



# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
# """процесс кодирования записей в json строку"""
# def encode():
#     model = WomenModel('Ange Jol', 'it"s content')
#     model_sr = WomenSerializer(model) # перобразование объекта в словарь
#     print(model_sr.data, type(model_sr), sep='\n')
#     json = JSONRenderer().render(model_sr.data) # преобразование в  байтовую строку в json формате
#     print(json)
#
# """процесс декодирования из json строки в записи """
# def decode(): # проверь в shell
#     stream = io.BytesIO(b'{"title":"Ange Jol", "contenct": "it is a content"}') #переданная json строка
#     data = JSONParser().parse(stream) # парсинг json строки
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data) #успешно проверенные переданные данные
