from django.shortcuts import render,HttpResponseRedirect
from .forms import Registration,Edituserchangeform ,Editadminchangeform
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm ,SetPasswordForm
from django.contrib.auth import authenticate, login,logout ,update_session_auth_hash
# Create your views here.
def user_signup(request):
  if request.method == "POST":
    fm = Registration(request.POST)
    if fm.is_valid():
      fm.save()
  else :
   fm = Registration()    
  return render(request,'enroll/signup.html',{'form':fm})

# login views funtion
def user_signin(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
     fm = AuthenticationForm(request=request,data=request.POST)
     if fm.is_valid():
      uname = fm.cleaned_data['username']
      upass = fm.cleaned_data['password']
      User = authenticate(username=uname,password=upass)
      if User is not None :
        login(request,User)
        return HttpResponseRedirect('/profile/')
    else :
     fm = AuthenticationForm()
    return render(request,'enroll/signin.html' ,{'form':fm})    
  else :
    return HttpResponseRedirect('/profile/')

# profile vieews function 
def user_profile(request):
  if request.user.is_authenticated:
    if request.method =="POST":
      if request.user.is_superuser == True:
        fm = Editadminchangeform(request.POST ,instance=request.user)
      else :
        fm = Edituserchangeform(request.POST ,instance=request.user)    
      if fm.is_valid():
        fm.save()
    else:
      if request.user.is_superuser == True:
        fm = Editadminchangeform(instance=request.user) 
      else :
        fm = Edituserchangeform(instance=request.user) 
           
    return render(request,'enroll/profile.html',{'name':request.user ,'form':fm}) 
  else :
    return HttpResponseRedirect('/signin/')
# logout views function
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/signin/')       

# change with old password 
def user_changepass(request):
  if request.user.is_authenticated:
    if request.method =="POST":
      fm = PasswordChangeForm(user=request.user , data=request.POST)
      if fm.is_valid():
        fm.save()
        update_session_auth_hash(request,fm.user)
        return HttpResponseRedirect('/profile/')
    else :
      fm = PasswordChangeForm(user = request.user)    
    return render(request,'enroll/changepass.html',{'form':fm})
  else :
    return HttpResponseRedirect('/login/')

# change without old password 
def user_changepass1(request):
  if request.user.is_authenticated:
    if request.method =="POST":
      fm = SetPasswordForm(user=request.user , data=request.POST)
      if fm.is_valid():
        fm.save()
        update_session_auth_hash(request,fm.user)
        return HttpResponseRedirect('/profile/')
    else :
      fm = SetPasswordForm(user = request.user)    
    return render(request,'enroll/changepass1.html',{'form':fm})
  else :
    return HttpResponseRedirect('/login/')    