from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UserCreateForm, LoginForm, UserUpdateForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from user_app.models import User


class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = ''


class UserCreate(TemplateView):
    template_name = 'user_app/form.html'

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
    template_name = 'user_app/login.html'

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
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('password', 'Invalid email or password')
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})


class UserLogout(MyLoginRequiredMixin, TemplateView):

    def get(self, request):
        logout(request)
        return redirect('login')


class UserUpdate(MyLoginRequiredMixin, TemplateView):
    template_name = 'user_app/updateform.html'

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
        return render(request, 'user_app/updateform.html', {'form': form})
