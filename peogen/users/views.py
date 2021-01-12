from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserModel
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    UserChangePasswordForm
)

from .tasks import user_registered


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request=request, message=f'Account created for {username}!')

            print(user.id)
            user_registered.delay(user_id=user.id)
            return HttpResponse("Please confirm your email address to complete the registration")
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request=request, template_name='users/register.html', context=context)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        group = Group.objects.get(name="viewer")
        user.groups.set([group])
        return HttpResponse("Thank you for your email confirmation. Now you can login your account.")
    else:
        return HttpResponse("Activation link is invalid.")


@login_required
def profile(request):

    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request=request, message=f'Your account has been updated!')
            return redirect('profile')

    else:

        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request=request, template_name='users/profile.html', context=context)


def change_password(request):
    if request.method == "POST":
        form = UserChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            message.success(request, 'Your password has been updated!')
            return redirect("change_password")
        else:
            message.error(request, "Please correct the error below.")
    else:
        form = UserChangePasswordForm(request.user)

    context = {
        'form': form
    }
    return render(request=request, template_name="users/change_password.html", context=context)