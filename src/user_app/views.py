from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from pprint import pprint
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    form = RegistrationForm(request.POST or None)
    if request.user.is_authenticated:
        messages.warning(request, "You already have an account!")
        return redirect('main:post_list')

    if form.is_valid():
        form.save()
        name = form.cleaned_data['username']
        messages.success(request, f'Account created for {name}!')
        return redirect('login')
    context = {
        'form': form
    }

    return render(request, 'user_app/register.html', context)

@login_required()
def display_profile_page(request):
    user_form = UserUpdateForm(request.POST or None, instance=request.user)
    profile_form = ProfileUpdateForm(
        request.POST or None, request.FILES or None, instance=request.user.profile)

    pprint(request.user)
    
    # def update_profile():
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(request, "Your profile has been updated!")
        return redirect(request.path)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'user_app/profile_page.html', context)
