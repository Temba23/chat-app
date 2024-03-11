from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('<str:room>/', room, name="room"),
    path('getMessages/<str:room>/', getMessages, name="getMessages"),
    path('checkview', checkview, name="checkview"),
    path('send', send, name="send"),
]