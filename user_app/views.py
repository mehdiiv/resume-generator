from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import (
    UserCreateForm, LoginForm,
    UserUpdateForm, UserInformationForm
    )
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from user_app.models import User


class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = ''


class UserCreate(TemplateView):
    template_name = 'user_app/create_form.html'

    def get(self, request):
        context = {'UserCreateForm': UserCreateForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})


class UserLogin(TemplateView):
    template_name = 'user_app/login_form.html'

    def get(self, request):
        context = {
            'loginform': LoginForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                form.add_error('email', 'Invalid email or password')
                return render(request, self.template_name, {'form': form})
            if user.check_password(password):
                login(request, user)
                return redirect('home')
            else:
                form.add_error('password', 'Invalid email or password')
                return render(request, self.template_name, {'form': form})
        else:
            return redirect('login')


class UserLogout(MyLoginRequiredMixin, TemplateView):

    def get(self, request):
        logout(request)
        return redirect('login')


class UserUpdate(MyLoginRequiredMixin, TemplateView):
    template_name = 'user_app/manage_account_form.html'

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        context = {'form': UserUpdateForm(instance=user)}
        return render(request, self.template_name, context)

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user = form.save()
            return redirect('home')
        return render(
            request, 'user_app/manage_account_form.html', {'form': form}
            )


class ProfileInformation(
    MyLoginRequiredMixin, TemplateView
        ):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        return render(
            request, 'user_app/profile_information.html', {'user': user}
            )


class EditProfileInformation(MyLoginRequiredMixin, TemplateView):
    template_name = 'user_app/profile_information_form.html'

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        context = {'form': UserInformationForm(instance=user)}
        return render(request, self.template_name, context)

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        form = UserInformationForm(
            request.POST, request.FILES, instance=user
            )
        if form.is_valid():
            user = form.save()
            return render(
                request, 'user_app/profile_information.html', {'user': user}
                )
        return render(
            request, 'user_app/profile_information_form.html', {'form': form}
            )
class Counter:
    def __init__(self, count=0, max=5):
        self.count = count
        self.max = max

    def increment(self):
        self.count += 1
        return self.count % self.max

class UserResumeView(TemplateView):
    template_name = 'user_app/resume.html'

    def get(self, request, full_name):
        try:
            first_name, last_name = full_name.split('-', 1)
            user = User.objects.get(first_name=first_name, last_name=last_name)
            color_number = Counter(0)
            context = {'color_number': color_number, 'user': user}
            return render(request, self.template_name, context)
        except (ValueError, User.DoesNotExist):
            return redirect('not_found_auth')
