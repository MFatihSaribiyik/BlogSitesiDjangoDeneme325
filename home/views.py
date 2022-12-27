from django.http import HttpResponse
from django.shortcuts import render

from blog.models import ContackFormu, Blog
from home.models import Setting


# Create your views here.
#def index(request):
    #text="Merhaba yarra bandıı ben views.py nin içinden text halinde gledim <br> proje oluşturma:django-admin start poject mysite <br> app ekleme: python manage.py startapp polls" #texti indexteki texe yolladım burda ne yazarsam gidyo
    #context = {'text': text}
    #return render(request, 'index.html', context)


def index(request):
    #contack = ContackFormu.objects.all() estting teki gibi contak formum yok
    setting = Setting.objects.get(pk=1) #pk yı 0 yapinca hata veriyor pk daki verilerin sırası ben 2. başlığı çekmek istersem pk 2 olcak
    #text="Merhaba bandıı ben views.py nin içinden text halinde gledim <br> proje oluşturma:django-admin start poject mysite <br> app ekleme: python manage.py startapp polls" #texti indexteki texe yolladım burda ne yazarsam gidyo
    category=Category.objects.all()
    context = {'setting': setting,
               'category':category}
    return render(request, 'index.html', context)
#bu şeyi yukarıdakine yazınca hat averiyor
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Category
from home.models import Setting


# Create your views here.
def user_profile(request):
    category=Category.objects.all()
    settings=Setting.objects.filter(pk=0)
    context ={
        'category':category,
        'settings':settings
    }
    return render(request,'user_profile.html',context) #contaksayfasını görmüyor çünkü 2 tane ana sayfam var


def category_blog(request , id , slug):#bu bağımsız olan altta bağımlı blogS var
    category = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)#buraya id yazınca aynı hatayı veriyo
    blog = Blog.objects.filter(category_id=id)#buraya id yazınca olmuyor hata: id yerine sayı bekleniyordu
    context = {
        'selectedCategory': selectedCategory,
        'category': category,
        'blog': blog
    }
    return render(request, 'blogBilgiDeneme.html', context)


def category_blogs(request,id,slug):
    category = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    blog = Blog.objects.filter(category_id=id)

    context ={
        'selectedCategory': selectedCategory,
        'category':category,
        'blog':blog,
    }
    return render(request,'blogs.html',context)