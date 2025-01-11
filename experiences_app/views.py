from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from experiences_app.models import Experience
from user_app.views import MyLoginRequiredMixin
from experiences_app.forms import ExperienceForm


class ExperienceListView(MyLoginRequiredMixin, TemplateView):

    def get(self, request):
        experiences = request.user.experiences.all()
        return render(
            request, 'experiences/list.html',
            {'experiences': experiences}
            )


class ExperienceCreateView(MyLoginRequiredMixin, TemplateView):
    template_name = 'experiences/new_and_edit.html'

    def get(self, request):
        context = {'form': ExperienceForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            experiences = request.user.experiences.all()
            return redirect('experiences_list')
        return render(request, self.template_name, {'form': form})


class ExperienceDeleteView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk_experience):
        try:
            request.user.experiences.get(id=pk_experience).delete()
            return redirect('experiences_list')
        except Experience.DoesNotExist:
            return redirect('not_found')


class ExperienceEditView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk_experience):
        try:
            experience = request.user.experiences.get(id=pk_experience)
            context = {'form': ExperienceForm(instance=experience)}
            return render(
                request, 'experiences/new_and_edit.html', context
                )
        except Experience.DoesNotExist:
            return redirect('not_found')

    def post(sefl, request, pk_experience):
        experience = request.user.experiences.get(id=pk_experience)
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('experiences_list')
        return render(
            request, 'experiences/new_and_edit.html', {'form': form}
            )
