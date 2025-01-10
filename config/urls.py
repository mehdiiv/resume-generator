from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [

    path('', include('user_app.urls')),
    path('Categories/', include('skill.urls')),
    path('404', TemplateView.as_view(template_name='404.html'),
         name='not_found'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
