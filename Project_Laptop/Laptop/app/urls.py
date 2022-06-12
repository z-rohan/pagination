from django.urls import path
from .views import *

urlpatterns=[
    path('ev/',LaptopView, name='lapform_url'),
    path('sl/',ShowLaptop,name='showlap_url'),
    path('sl/<int:page>/',ShowLaptop,name='showlap_url'),
    path('uv/<int:id>/',UpdateLaptopView,name='update_url'),
    path('dv/<int:id>/',DeleteLaptopView,name='delete_url'),
]


