from django.shortcuts import render,redirect
from . import forms
from Blog.models import BlogPost

def register_page(request):
    form=forms.UserRegisterForm()
    
    if request.method=="POST":
        form=forms.UserRegisterForm(request.POST)
        print('POSt')
        if form.is_valid():
            print('is valid')
            form.save()
            return redirect('login')

    return render(request,'user/register.html',{'form':form})


# def login_page(request):
#     form=forms.UserRegisterForm()

#     return render(request,'user/register.html',{'form':form})

