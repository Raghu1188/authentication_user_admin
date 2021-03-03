from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User

class Registration(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','first_name','last_name','email',]


class Edituserchangeform(UserChangeForm):
  password = None 
  class Meta :
    model = User 
    fields = ['username','first_name','last_name','email','date_joined', 'last_login']    
 

class Editadminchangeform(UserChangeForm):
  password = None
  class Meta :
    model = User 
    fields = "__all__"  