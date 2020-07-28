from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'about_us.html')

def gallary(request):
    product=Product.objects.all()
    return render(request,'gallary.html',{'prod':product})

def contactus(request):
    return render(request,'index.html')

def menu(request):
    return render(request,'menu.html')

def contact_us_form(request):
    if request.method =='POST':
        full_name=request.POST['full_name']
        mobile_no = request.POST['mobile_no']
        email = request.POST['email']
        comment = request.POST['comment']

        user=pooja_caterers_form(full_name=full_name,mobile_no=mobile_no,email=email,comment=comment)
        user.save()
        return redirect('home')
