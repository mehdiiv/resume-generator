from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from user_app.models import User


class Counter:
    def __init__(self, count=0, max=5):
        self.count = count
        self.max = max

    def increment(self):
        self.count += 1
        return self.count % self.max

class UserResumeView(TemplateView):
    template_name = 'resume/resume.html'

    def get(self, request, full_name):
        try:
            first_name, last_name = full_name.split('-', 1)
            user = User.objects.get(first_name=first_name, last_name=last_name)
            color_number = Counter(0)
            context = {'color_number': color_number, 'user': user}
            return render(request, self.template_name, context)
        except (ValueError, User.DoesNotExist):
            return redirect('not_found_auth')
