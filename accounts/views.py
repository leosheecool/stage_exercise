from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


#Valid_form_with_email

from .form import CustomUserCreationForm, EditProfileForm

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('signup')

    else:
        f = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': f})

def profile(request):
    arguments = {'user': request.user}
    return render(request, 'profile.html', arguments)

def profile_editor1(request):
    if request.method == "POST":
        change_form = EditProfileForm(request.POST, instance=request.user)

        if change_form.is_valid():
            change_form.save()
            return redirect('profile')
        else:
            change_form = EditProfileForm()
            arguments = {'user': request.user, 'form': change_form}
            return render(request, 'edit_profile.html', arguments)
    else:
        change_form = EditProfileForm(instance=request.user)
        arguments = {'user': request.user, 'form': change_form}
        return render(request, 'edit_profile.html', arguments)