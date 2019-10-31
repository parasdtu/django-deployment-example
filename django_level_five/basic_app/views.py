from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm



#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    registered=False
    if request.method=="POST":
        profile_form=UserProfileInfoForm(data=request.POST)
        user_form=UserForm(data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)#this line hashes the password into unique code
            user.save()

            profile=profile_form.save(commit=False) #That's useful when you get most of your model data from a form, but need to populate some null=False fields with non-form data. Saving with commit=False gets you a model object, then you can add your extra data and save it.
            profile.user=user#this line of code means that, the profile will not override the data in user form but will form a OneToOneField relation with user.

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']#sutax code for saving profile_pic

            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request,'basic_app/registration.html',
                    {'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered})

@login_required
def special(request):
    return HttpResponse("you re logged in ;)")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Invalid Username or Password!")

        else:
            print("login failed!")
            return HttpResponse("invalid login details.")

    else:
        return render(request,'basic_app/login.html',{})
