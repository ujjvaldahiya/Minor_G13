from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from users import models
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def change_password(request):
        if request.method == 'POST':
            obj = User.objects.get(username__exact=request.user.username)
            if obj.check_password(request.POST['oldpassword']):
                if request.POST['newpassword'] == request.POST['cpassword']:
                    obj.set_password(request.POST['newpassword'])
                    obj.save()
                    error = 'Password Changed Successfully!'
                else:
                    error = 'New Password and Confirm Password fields do not match!'
            else:
                error = 'Incorrect Old Password!'
        else:
            error = 'None'

        return render(request, 'users/change_password.html', {'error': error})
