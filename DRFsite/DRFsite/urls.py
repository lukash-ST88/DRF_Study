"""DRFsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from women.views import *
from .myrouters import MyCusomRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = routers.SimpleRouter()
# router = routers.DefaultRouter() # отличается от SimpleRouter() наличием маршрута по умолчанию (api/v1/)
router.register(r'women', WomenAPIViewSet, basename='girls') # basename по умолчанию берется из queryset представления
router2 = MyCusomRouter()
router2.register(r'custwomen', WomenAPIViewSet, basename='custgirls')
print(router.urls)
print((router2.urls))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')), #аутентификация по сессиям (session-authentication)
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')), #url авторизации по токенам
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router2.urls)),
    path('api/v1/womenlist/', WomenAPIList.as_view()),
    path('api/v1/womenupdate/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendestroy/<int:pk>/', WomenAPIDestroy.as_view()),
    path('api/v1/womendetail/<int:pk>/', WomenAPIdetail.as_view()),

    # path('api/v1/womenlist/', WomenAPIViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIViewSet.as_view({'put' : 'update'})),
]
