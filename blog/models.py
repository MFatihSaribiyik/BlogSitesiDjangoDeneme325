from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea


# Create your models here.
#adam satış kodları koymuş blog ekliyemiyom aw ben

class Category(models.Model):
    STATUS=(
        ("True","False"),
        ("False" ,"True"),
    )
    title= models.CharField(max_length=30) #uzunluk
    keywords =models.CharField(max_length=225) #alan türü
    description =models.CharField(max_length=255) #alantürü
    image=models.ImageField(blank=True, upload_to="images/") #buraya iamge dosya eklenecek
    status=models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField() #adres satırı id değil yazı ile çağırma
    parent = models.ForeignKey("self", blank=True , null=True ,related_name="children" , on_delete=models.CASCADE) #bu silinirse alt doyada silinsin bağlantılı#kadegori alt katekogori iç içe
    create_at =models.DateTimeField(auto_now_add=True) #ne zman oluşturuldu
    update_at = models.DateTimeField(auto_now=True) #ne zaman upload edildi

    def __str__(self):
        return self.title

    #def __str__(self):  # category parent kısmında alt üyeyi gösteriyo bu return
     #   full_path = [self.title]
      #  k = self.parent
       # while k is not None:
        #    full_path.append(k.title)
         #   k = k.parent
        #return '->'.join(full_path[::-1])
        #hocam resim linklerini id ile yollamada adam while döngüsünü yazamamış admini bozuyo kodalr eski haline getirdim

class Blog(models.Model):
    STATUS = (
        ("True", "Evet"),
        ("False", "Hayır"),
    )
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    price = models.FloatField()
    amouth = models.IntegerField()
    detail = models.TextField()
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.TimeField(auto_now=True)
    def __str__(self):
        return self.title

class Images(models.Model):

    blog=models.ForeignKey(Blog ,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image =models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title

class ContackFormMessage(models.Model):
    STATUS = (
        ("True", "Evet"),
        ("False", "Hayır"),
    )
    name=models.CharField(blank=True,max_length=20)
    email=models.CharField(blank=True ,max_length=50)
    subject=models.CharField(blank=True,max_length=50)
    message =models.CharField(blank=True,max_length=255)
    status= models.CharField(choices=STATUS,max_length=10,default='New')
    ip =models.CharField(blank=True,max_length=20)
    note=models.CharField(blank=True,max_length=200)
    phoneNumber=models.CharField(blank=True,max_length=11)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ContackFormu(ModelForm):
    class Meta:
        model=ContackFormMessage
        fields=['name','email','phoneNumber','message']
   #     widgets={
    #        'name'  :TextInput(attrs={'class':'form_contril','placeholder':'Name'}),
     #       'phoneNumber'   :TextInput(attrs={'class':'form_contril','placeholder':'phoneNumber'}),
      #      'email'       :TextInput(attrs={'class':'form_contril','placeholder':'email'}),
       #     'message'   :Textarea(attrs={'class':'textarea','placeholder':'message'}),
        #}


class Comment(models.Model):
    STATUS =(
        ('New', 'Yeni'),
        ('True','Evet'),
        ('False', 'Hayır'),
    )
    blog =models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=200,blank=True)
    rate = models.IntegerField(blank=True)
    status=models.CharField( max_length=20,choices=STATUS,default='new')
    ip = models.CharField(blank=True,max_length=20)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

#comment profile bozuk ekleyemedim
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['subject','comment','rate']