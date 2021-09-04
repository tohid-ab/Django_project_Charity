from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


class PasswordChangeViewe(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    template_name = 'registration/password_change.html'


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class RegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)


class ProfileView(UpdateView):
    form_class = UserChangeForm
    success_url = reverse_lazy("home")
    template_name = 'registration/profile.html'

    def dispatch(self, request, *args, **kwargs):
        Profile.objects.get_or_create(user=request.user)
        if not request.user.is_authenticated:
            return redirect('login')
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user


class ProfileChangeView(UpdateView):
    form_class = UserChangeForm
    success_url = reverse_lazy("profile_success")
    template_name = 'registration/profile_change.html'

    def get_object(self):
        return self.request.user


def profile_success(request):
    return render(request, 'registration/profile_success.html', {})


@login_required()
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/profile_image.html', context)


def image_success(request):
    return render(request, 'registration/profile_success.html', {})