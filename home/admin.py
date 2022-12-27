from django.contrib import admin

from home.models import Setting, UserProfile

# Register your models here.
#class blogAdmin(admin.ModelAdmin):      ben resimi stemiyom
#    readonly_fields = ('iamge_tag')


admin.site.register(UserProfile)

admin.site.register(Setting)
