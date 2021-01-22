from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Profile
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from pprint import pprint

# Create your views here.


def register(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')
    context = {
        'form': form
    }

    return render(request, 'user_app/register.html', context)


def display_profile_page(request):
    user_form = UserUpdateForm(request.POST or None, instance=request.user)
    profile_form = ProfileUpdateForm(
        request.POST or None, request.FILES or None, instance=request.user.profile)

    pprint(request.user)
    
    # def update_profile():
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect(request.path)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'user_app/profile_page.html', context)
