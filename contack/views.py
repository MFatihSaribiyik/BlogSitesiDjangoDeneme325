from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Category
from home.models import Setting


# Create your views here.
def index(request):
    category=Category.objects.all()
    settings=Setting.objects.filter(pk=0)
    context ={
        'category':category,
        'settings':settings
    }
    return render(request,'contackSayfasi.html',context) #contaksayfasını görmüyor çünkü 2 tane ana sayfam var



