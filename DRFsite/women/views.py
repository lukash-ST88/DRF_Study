from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Women, Category
from .serializers import WomenSerializer
from .permissions import IsAdminOrReadOnlyCust, IsOwnerOrReadOnlyCust
from rest_framework_simplejwt.authentication import JWTAuthentication
from .paginations import WomenPaginationAPI

"""совмещает в себе все классы по работе с данными конкретной модели"""
class WomenAPIViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk') # для возврата одной записи по pk
        if not pk:
            return Women.objects.all().order_by('-pk')[:3] #последние три записи
        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def categories(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]}) #выводим список категорий

    @action(methods=['get', 'put', 'post'], detail=True)
    def category(self, request, pk):
        cats = Category.objects.get(pk=pk)
        return Response({'cat': cats.name})


"""отдельные калассы по рабтое с данными моделей"""
class WomenAPIList(generics.ListCreateAPIView):  # класс позволяет создавать и возвращать список данных
    queryset = Women.objects.all()  # данные возвращаемые по запросу
    serializer_class = WomenSerializer  # обработка выбранных полей этих данных в JSON формат
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenPaginationAPI

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()  # это ленивый запрос поэтому возвращается только одна измненная запись
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnlyCust,)
    authentication_classes = (TokenAuthentication,) #доступ к изменению получают только пользователи авторизированные по токену

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()  # это ленивый запрос поэтому возвращается только одна измненная запись
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnlyCust,)
    authentication_classes = (JWTAuthentication,) # доступ к удалению получают только для авторизованные пользователи по JWT


"""общий класс"""
class WomenAPIdetail(generics.RetrieveUpdateDestroyAPIView):  # работа с отдельной записью
    queryset = Women.objects.all()
    serializer_class = WomenSerializer



# """что находится под капотом классов list create update"""
# class WomenAPIView(APIView):
#
#     def get(self, request):  # создание get запроса
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data}) #здесь many говорит об обратботке множества записей, а не одной
#
#     #  а .data преобразует все в список из словарей преобразованных данных из таблицы womenf
#
#     def post(self, request):  # создание post запроса. Создание записи и вывод ее на экран
#         serializer = WomenSerializer(data=request.data) #распоковка json файлов, переданных пользователем
#         serializer.is_valid(raise_exception=True) #проверка корректности ввода данных пользователем
#         serializer.save()  # сохранение данных через метод create класса WomenSerializer
#         return Response({'create': serializer.data}) #проебразование модели в словарь для JSON файла
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None) # если нет подходящего pk то пишем none
#         if pk is None:
#             return Response({'error': 'Method PUT not allowed'})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': "Object does not exist"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() # вызывает метод update так как в сериализатор переданы параметры data и instance
#         return Response({"post": serializer.data})
#     """версия без сериализатора"""
# def get(self, request):  # создание get запроса
#     lst = Women.objects.all().values()
#     return Response({'posts': list(lst)})  # преобразует словарь в  байтовую JSON строку

# def post(self, request):  # создание post запроса. Создание записи и вывод ее на экран
#     crt = Women.objects.create(
#         title=request.data['title'],
#         content=request.data['content'],
#         cat_id=request.data['cat_id'])
#      return Response({'create': WomenSerializer(crt).data}) #проебразование модели в словарь для JSON файла


