from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Profile, Recipe,Category
from django.forms import ModelForm, TextInput, EmailInput,ImageField, Textarea



class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class UpdateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

