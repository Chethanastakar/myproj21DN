import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproj19.settings')
import django
django.setup()

from faker import Faker
from CustomerApp.models import *
from random import *
fake=Faker()

def get_phoneno():
    s1=randint(7,9)
    num=str(s1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fcname=fake.name()
        fcid=fake.random_int(min=1,max=999)
        fbal=fake.random_int(min=10000,max=99999)
        fdob=fake.date()
        femail=fake.email()
        fphoneno=get_phoneno()
        faddress=fake.address()
        cust_record=Customer.objects.get_or_create(cname=fcname,cid=fcid,bal=fbal,dob=fdob,email=femail,phoneno=fphoneno,address=faddress)
populate(30)
