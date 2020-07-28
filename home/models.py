from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.

class pooja_caterers_form(models.Model):
    full_name=models.CharField(max_length=20)
    mobile_no=PhoneNumberField()
    email=models.EmailField(max_length=30)
    comment=models.CharField(max_length=300)
    def __str__(self):
        return self.full_name

class Product(models.Model):
    number=models.IntegerField(max_length=10,null=True,blank=True)
    img=models.ImageField(upload_to='static/images',null=True)

    

    





