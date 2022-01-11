from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
# Создаем router и регистрируем ViewSet
router = DefaultRouter()
router.register(r'posts', views.PostList)
# URLs настраиваются автоматически роутером
urlpatterns = router.urls


