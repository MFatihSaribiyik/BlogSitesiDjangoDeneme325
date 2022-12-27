from django.http import HttpResponse
from django.shortcuts import render

from home.models import UserProfile, Setting


# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1) #buraya pk dosyası eklersen bozuluyor
    user = UserProfile.objects.contains(request.user)
    context= {
    'user':user,
    'setting':setting,}
    return render(request,'user_profile.html',context)