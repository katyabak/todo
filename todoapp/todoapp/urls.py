from django.contrib import admin
from django.urls import path, include

# подключение приложений
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')), # главная страница
    path('users/', include('users.urls')),  # маршруты пользователей
]