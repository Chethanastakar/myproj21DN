from django.contrib import admin
from CustomerApp.models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['cid','cname','bal','dob','email','phoneno','address']
admin.site.register(Customer,CustomerAdmin)
