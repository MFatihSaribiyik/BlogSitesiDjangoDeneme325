from django.contrib import admin
#contack Form message burda zaten varmış import edince olmadı,Conrack from messageyi aşşağıda bişeler yazdım kendi etti import
from blog.models import Category, Blog, Images, ContackFormMessage, Comment


class BlogImageInline(admin.TabularInline):
    model = Images
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category','price','image','amouth', 'status'] #amounth eklenmiyor???? amount muş
    list_filter = ['status','category']
    inlines = [BlogImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','image','blog']

class ContackFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','phoneNumber','email','status']
    list_filter = ['status']
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','user','status','blog']
    list_filter = ['status']
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(ContackFormMessage,ContackFormMessageAdmin)

