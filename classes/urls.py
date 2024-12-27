from django.urls import path, include
from rest_framework import routers

from .views import *


urlpatterns = [
    path('education/', EducationAPIList.as_view()),
    path('education/<int:pk>/', EducationAPIUpdate.as_view()),
    path('education/create/', EducatioAPICreate.as_view()),
    path('educationdelete/<int:pk>/', EducationAPIDestroy.as_view()),

    path('job/', JobAPIList.as_view()),
    path('job/<int:pk>/', JobAPIUpdate.as_view()),
    path('job/<int:pk>/', JobAPIDestroy.as_view()),
    path('job/create/', JobAPICreate.as_view()),

    path('application/', ApplicantionAPIList.as_view()),
    path('application/<int:pk>/', ApplicantionAPIUpdate.as_view()),
    path('application/<int:pk>/', ApplicantionAPIDestroy.as_view()),
    path('application/create/', ApplicantionAPICreate.as_view()),


    path('vacancy/', VacancyAPIList.as_view()),
    path('vacancy/<int:pk>/', VacancyAPIUpdate.as_view()),
    path('vacancy/<int:pk>/', VacancyAPIDestroy.as_view()),
    path('vacancy/create/', VacancyAPICreate.as_view()),
]