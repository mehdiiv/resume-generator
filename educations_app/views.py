from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from educations_app.models import Education, EducationDescription
from user_app.views import MyLoginRequiredMixin
from educations_app.forms import EducationForm, EducationDescriptionForm


class EducationListView(MyLoginRequiredMixin, TemplateView):

    def get(self, request):
        educations = request.user.educations.all()
        return render(
            request, 'educations/list.html',
            {'educations': educations}
            )


class EducationCreateView(MyLoginRequiredMixin, TemplateView):
    template_name = 'educations/new_and_edit.html'

    def get(self, request):
        context = {'form': EducationForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = EducationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('educations_list')
        return render(request, self.template_name, {'form': form})


class EducationDeleteView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk_education):
        try:
            request.user.educations.get(id=pk_education).delete()
            return redirect('educations_list')
        except Education.DoesNotExist:
            return redirect('not_found')


class EducationEditView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk_education):
        try:
            education = request.user.educations.get(id=pk_education)
            context = {'form': EducationForm(instance=education)}
            return render(
                request, 'educations/new_and_edit.html', context
                )
        except Education.DoesNotExist:
            return redirect('not_found')

    def post(sefl, request, pk_education):
        education = request.user.educations.get(id=pk_education)
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('educations_list')
        return render(
            request, 'educations/new_and_edit.html', {'form': form}
            )
class EducationDetailView(MyLoginRequiredMixin, TemplateView):
    template_name = 'educations/detail.html'

    def get(self, request, pk_education):
        try:
            education = request.user.educations.get(id=pk_education)
            descriptions = EducationDescription.objects.all().filter(education_id=pk_education)
            context = {
                'education_object': education,
                'descriptions_ojecsts': descriptions
                }
            return render(
                request, self.template_name, context
                )
        except Education.DoesNotExist:
            return redirect('not_found')


class EducationDescriptionCreateView(MyLoginRequiredMixin, TemplateView):
    template_name = 'education_descriptions/new_and_edit.html'

    def get(self, request, pk_education):
        try:
            request.user.educations.get(id=pk_education)
            context = {'form': EducationDescriptionForm}
            return render(request, self.template_name, context)
        except Education.DoesNotExist:
            return redirect('not_found')

    def post(self, request, pk_education):
        try:
            request.user.educations.get(id=pk_education)
            form = EducationDescriptionForm(request.POST)
            form.instance.education_id = pk_education
            if form.is_valid():
                form.save()
                return redirect('education_detail', pk_education)
            return render(request, self.template_name, {'form': form})
        except Education.DoesNotExist:
            return redirect('not_found')


class EducationDescriptionDeleteView(MyLoginRequiredMixin, TemplateView):

    def get(self, request, pk_education, pk_education_description):
        try:
            education = request.user.educations.get(id=pk_education)
            education.education_descriptions.get(id=pk_education_description).delete()
            return redirect('education_detail', pk_education)
        except (Education.DoesNotExist, EducationDescription.DoesNotExist):
            return redirect('not_found')


class EducationDescriptionEditView(MyLoginRequiredMixin, TemplateView):
    template_name = 'education_descriptions/new_and_edit.html'

    def get(self, request, pk_education, pk_education_description):
        try:
            education = request.user.educations.get(id=pk_education)
            educationdescription = education.education_descriptions.get(id=pk_education_description)
            form = EducationDescriptionForm(instance=educationdescription)
            context = {'form': form}
            return render(
                request, self.template_name, context
            )
        except (Education.DoesNotExist, EducationDescription.DoesNotExist):
            return redirect('not_found')

    def post(self, request, pk_education, pk_education_description):
        try:
            education = request.user.educations.get(id=pk_education)
            educationdescription = education.education_descriptions.get(id=pk_education_description)
            form = EducationDescriptionForm(request.POST, instance=educationdescription)
            if form.is_valid():
                form.save()
                return redirect('education_detail', pk_education)
            return render(
                request, self.template_name, {'form': form}
            )
        except (Education.DoesNotExist, EducationDescription.DoesNotExist):
            return redirect('not_found')
