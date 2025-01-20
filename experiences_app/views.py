from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from experiences_app.models import Experience, ExperienceDescription
from user_app.views import MyLoginRequiredMixin
from experiences_app.forms import ExperienceForm, ExperienceDescriptionForm


class ExperienceListView(MyLoginRequiredMixin, TemplateView):

    def get(self, request):
        experiences = request.user.experiences.all()
        return render(
            request, 'experiences/list.html',
            {'experiences': experiences}
            )


class ExperienceCreateView(MyLoginRequiredMixin, TemplateView):
    template_name = 'experiences/new.html'

    def get(self, request):
        context = {'form': ExperienceForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            request.user.experiences.all()
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
                request, 'experiences/edit.html', context
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
            request, 'experiences/edit.html', {'form': form}
            )


class ExperienceDetailView(MyLoginRequiredMixin, TemplateView):
    template_name = 'experiences/detail.html'

    def get(self, request, pk_experience):
        try:
            experience = request.user.experiences.get(id=pk_experience)
            descriptions = ExperienceDescription.objects.all().filter(experience_id=pk_experience)
            context = {
                'experience_object': experience,
                'descriptions_ojecsts': descriptions
                }
            return render(
                request, self.template_name, context
                )
        except Experience.DoesNotExist:
            return redirect('not_found')


class ExperienceDescriptionCreateView(MyLoginRequiredMixin, TemplateView):
    template_name = 'experience_descriptions/new_and_edit.html'

    def get(self, request, pk_experience):
        try:
            request.user.experiences.get(id=pk_experience)
            context = {'form': ExperienceDescriptionForm}
            return render(request, self.template_name, context)
        except Experience.DoesNotExist:
            return redirect('not_found')

    def post(self, request, pk_experience):
        try:
            request.user.experiences.get(id=pk_experience)
            form = ExperienceDescriptionForm(request.POST)
            form.instance.experience_id = pk_experience
            if form.is_valid():
                form.save()
                return redirect('experience_detail', pk_experience)
            return render(request, self.template_name, {'form': form})
        except Experience.DoesNotExist:
            return redirect('not_found')


class ExperienceDescriptionDeleteView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk_experience, pk_experience_description):
        try:
            experience = request.user.experiences.get(id=pk_experience)
            experience.experience_descriptions.get(id=pk_experience_description).delete()
            return redirect('experience_detail', pk_experience)
        except (Experience.DoesNotExist, ExperienceDescription.DoesNotExist):
            return redirect('not_found')


class ExperienceDescriptionEditView(MyLoginRequiredMixin, TemplateView):
    template_name = 'experience_descriptions/new_and_edit.html'

    def get(self, request, pk_experience, pk_experience_description):
        try:
            experience = request.user.experiences.get(id=pk_experience)
            experiencedescription = experience.experience_descriptions.get(id=pk_experience_description)
            form = ExperienceDescriptionForm(instance=experiencedescription)
            context = {'form': form}
            return render(
                request, self.template_name, context
            )
        except (Experience.DoesNotExist, ExperienceDescription.DoesNotExist):
            return redirect('not_found')

    def post(self, request, pk_experience, pk_experience_description):
        try:
            experience = request.user.experiences.get(id=pk_experience)
            experiencedescription = experience.experience_descriptions.get(id=pk_experience_description)
            form = ExperienceDescriptionForm(request.POST, instance=experiencedescription)
            if form.is_valid():
                form.save()
                return redirect('experience_detail', pk_experience)
            return render(
                request, self.template_name, {'form': form}
            )
        except (Experience.DoesNotExist, ExperienceDescription.DoesNotExist):
            return redirect('not_found')
