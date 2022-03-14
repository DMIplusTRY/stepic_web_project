from django.urls import path
from .views import test


urlpatterns = [
    path('', test, name='test'),
    path('login/', test, name='test'),
    path('singup/', test, name='test'),
    path('question/<int>/', test, name='test'),
    path('ask/', test, name='test'),
    path('popular/', test, name='test'),
    path('new/', test, name='test'),
]