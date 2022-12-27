from django.urls import  path

from blogBilgiDeneme import views

urlpatterns=[
    path('',views.index , name='index')
]