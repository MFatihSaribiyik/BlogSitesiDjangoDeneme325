from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


# Create your models here.
class Setting(models.Model):

    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    adress = models.CharField(max_length=500)
    icon = models.ImageField(blank=True ,upload_to='images/')
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=130)
    company = models.CharField(max_length=50)
    def __str__(self):
        return self.title
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(blank=True ,max_length=20)
    adres = models.CharField(blank=True, max_length=20)
    sehir = models.CharField(blank=True, max_length=20)
    ulke = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=300)

    def __str__(self):
        return self.user.first_name + ' ' +self.user.last_name

class UserProfileForm(ModelForm):
    class Meta:
        models=UserProfile
        fields =['phone','address']