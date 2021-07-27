from django.shortcuts import render
from CustomerApp.models import Customer
# Create your views here.
def customer_input(request):
    #customers=Customer.objects.all()
    #customers=Customer.objects.filter(bal__lt=20000,cname__startswith='A')
    #customers=Customer.objects.filter(bal__gt=20000,cname__startswith='A')
    customers=Customer.objects.all().order_by('-bal','bal')
    return render(request,'base.html',{'customers':customers})
