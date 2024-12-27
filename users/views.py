from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.views import CreateAPIView
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
    AllowAny
)

from .models import *
from .serializers import *
from .permissions import *


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny, ]
        elif self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'update':  
            permission_classes = [IsOwnerOrReadOnly, IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly]
        else: 
            permission_classes = [AllowAny]
        
        # return super(ApplicantViewSet, self).get_permissions()
        return [permission() for permission in permission_classes]

# class ApplicantCreateView(viewsets.CreateAPIView):
#     queryset = Applicant.objects.all()
#     serializer_class = ApplicantSerializer
#     permission_classes = [AllowAny, ]



    
class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

