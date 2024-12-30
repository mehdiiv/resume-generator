from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import render
from user_app.views import (
    UserCreate, UserLogin,
    UserLogout, MyLoginRequiredMixin,
    UserUpdate)


class HomeView(MyLoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, 'home.html')


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user/', UserCreate.as_view(), name='user'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('update/', UserUpdate.as_view(), name='update'),
]
