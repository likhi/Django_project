from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'your Account has been created. Now you can login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Register/register.html', {'form': form})


from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, profileUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = profileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # get request = url = profile/ = > Register /views.py/profile

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'Register/profile.html', context)