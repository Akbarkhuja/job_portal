from django.urls import path, include
from rest_framework import routers

from .views import *


applicant_router = routers.DefaultRouter()
applicant_router.register(r'applicants', ApplicantViewSet, basename='applicant')

recruiter_router = routers.SimpleRouter()
recruiter_router.register(r'recruiters', RecruiterViewSet, basename='recruiter')

[print(_url) for _url in applicant_router.urls]
print('\n\n')

urlpatterns = [
    path('', include(applicant_router.urls)),
    path('', include(recruiter_router.urls)),

    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),

    # path('login', LoginView.as_view(), name='login'),
    # path('user/', UserRecordView.as_view(), name='register_user'),

    # path('applicant/', ApplicantRecordView.as_view(), name='register_applicant'),
    # path('applicant/', ApplicantViewSet.as_view({'get': 'list'})),
    # path('applicant/<int:pk>/', ApplicantViewSet.as_view({'put':'update'})),

    # path('recruiter/', RecruiterRecordView.as_view(), name='register_recruiter'),
]