from django.urls import path,include
from . import views
from .  import *

urlpatterns = [
    path('messenger/',views.messenger , name= 'messenger'),
    path('messenger/sendsmscsv',views.sendsmscsv , name= 'msgcsv'),
    path('messenger/sendsms',views.sendsms , name = 'msgcomma'),
]