from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Category
from home.models import Setting


# Create your views here.
def index(request):
    category=Category.objects.all()
    setting=Setting.objects.get(pk=1)
    context ={
        'category':category,
        'settings':setting
    }
    return render(request,'hakkinda.html',context) #contaksayfasını görmüyor çünkü 2 tane ana sayfam var





