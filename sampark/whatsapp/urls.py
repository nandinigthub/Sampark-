from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('whatsapp/',views.whtsp,name = 'whtsp'),
    path('whatsapp/SendData',views.SendData),
]