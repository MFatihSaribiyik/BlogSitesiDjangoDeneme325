from django.shortcuts import render

from blog.models import Category, Blog


# Create your views here.




def index(request):
    category = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=1)#buraya id yazınca aynı hatayı veriyo
    blog = Blog.objects.filter(category_id=1)#buraya id yazınca olmuyor hata: id yerine sayı bekleniyordu
    context = {
        'selectedCategory': selectedCategory,
        'category': category,
        'blog': blog
    }
    return render(request, 'blogBilgiDeneme.html', context)