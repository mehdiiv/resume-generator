from django.urls import path
from resume_app.views import UserResumeView


urlpatterns = [
    path(
        '<slug:full_name>/',
        UserResumeView.as_view(), name='user_resume'
        )
]
