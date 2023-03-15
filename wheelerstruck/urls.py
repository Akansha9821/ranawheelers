from django.urls import path
from wheelerstruck import views


urlpatterns = [
    path('', views.index, name='wheelerstruckhome'),
]
