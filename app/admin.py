from django.contrib import admin
from app.models import Services

# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display=['id','name','price','is_active','pdetail']
    list_filter=['is_active']


admin.site.register(Services,ServicesAdmin)
