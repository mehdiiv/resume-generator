from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', include('user_app.urls')),
    path('skill/', include('skill.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
