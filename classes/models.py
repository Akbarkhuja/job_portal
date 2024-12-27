from django.db import models
from django.contrib.auth import get_user_model

from users.models import *

User = get_user_model()


class Profession(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Education(models.Model):
    TYPE = (
        ("undergraduate", "Undergraduate"),
        ("bachelor", "Bachelor"),
        ("master", "Master"),
        ("phd", "PhD")
    )

    university = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=TYPE)
    faculty = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Job(models.Model):

    JOB_TYPE = (
        ('1', "Full time"),
        ('2', "Part time"),
        ('3', "Internship"),
        ('4', "Online")
    )
    title = models.CharField(max_length=50)
    category =  models.ForeignKey(Profession, related_name='Category', on_delete=models.CASCADE)
    organization = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField(auto_now_add=True)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    position = models.ForeignKey(Profession, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_created=True)
    skills = models.TextField(max_length=500)



class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    position = models.ForeignKey(Profession, on_delete=models.CASCADE)
    organization  = models.ForeignKey(Organization, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_created=True)
    proposed_salary = models.FloatField()
    requirements = models.TextField(max_length=500)

    applied = models.ManyToManyField(Applicant)