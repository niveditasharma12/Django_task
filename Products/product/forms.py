from .models import Product
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


#class UserForm(UserCreationForm):
   # class Meta(UserCreationForm.Meta):
        #model = User

    #def __init__(self, *args, **kwargs):
        #super( self).__init__(*args, **kwargs)

        #for fieldname in ['username', 'password1', 'password2']:
            #self.fields[fieldname].help_text = None

    #def save(self, commit=True):
        #user = super().save(commit=False)
        #user.is_user = True
        #if commit:
            #user.save()
        #return user