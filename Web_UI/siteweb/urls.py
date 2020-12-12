from django.urls import path

from .views import *

app_name = "samir"

urlpatterns = [
    path('', home, name='home'),
    path('legal/', legal, name='legal'),
    path('contable/', contable, name='contable'),
    path('tributaria/', tributaria, name='tributaria'),
    path('startup/', startup, name='startup'),
    path('contact/', create_contact, name='contact'),
    path('news/', news, name='news'),
    path('about/', about, name='about'),
]