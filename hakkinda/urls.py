from django.urls import path

from hakkinda import views

urlpatterns=[
    path('' , views.index,name='index'),

]