from django.urls import path,include
from . import views
from .  import *

urlpatterns = [
    path('email/',views.email,name='email'),
    # path('email/emailcomma',views.emailcomma,name='emailcomma'),
    # path('email/emailcsv',views.emailcsv,name='emailcsv'),
    path('template/',views.template,name='template'),

]
