from django.urls import path
from app1.views import *
app_name='pooji'
urlpatterns=[
    path('janu/',janu,name='janu'),
]