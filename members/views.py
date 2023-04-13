from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# from .forms import SignUpForm, EditProfileForm, PasswordChangingForm

# Create your views here.
class PasswordsChangeView(PasswordChangeView): # PasswordChangeView must be imported from 
    form_class = PasswordChangeForm # PasswordChangeForm must be imported from django.contrib.auth.forms
    success_url = reverse_lazy('home')

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = './registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    # fields = '__all__'
    success_url = reverse_lazy('home')

    def get_object(self):
        ''' this will pass the current user '''
        return self.request.user