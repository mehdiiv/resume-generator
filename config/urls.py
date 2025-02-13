from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [

    path('', include('user_app.urls')),
    path('categories/', include('skill.urls')),
    path('experiences/', include('experiences_app.urls')),
    path('educations/', include('educations_app.urls')),
    path('resume/', include('resume_app.urls')),
    path('404', TemplateView.as_view(template_name='404.html'),
         name='not_found'),
    path('404_auth', TemplateView.as_view(template_name='404_auth.html'),
         name='not_found_auth'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
