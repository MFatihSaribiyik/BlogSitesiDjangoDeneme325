from django.http import HttpResponse
from django.shortcuts import render

from blog.models import ContackFormMessage
from home.models import Setting


# Create your views here.
#def index():
 #   return HttpResponse("Blog Page")

def index(request):
    centext= ContackFormMessage.objects.filter()#içine ne geliyo?
    setting = Setting.objects.filter(pk=0)
    #text="Merhaba yarra bandıı ben views.py nin içinden text halinde gledim <br> proje oluşturma:django-admin start poject mysite <br> app ekleme: python manage.py startapp polls" #texti indexteki texe yolladım burda ne yazarsam gidyo
    context = {'setting': setting}
    return render(request, 'index.html', context)
#bu şeyi yukarıdakine yazınca hat averiyor
