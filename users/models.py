from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)

    GENDER = (
        ('M', 'male'),
        ('F', 'female')
    )
    gender = models.CharField(choices=GENDER, max_length=10, blank=True, null=True)

    is_applicant = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Organization(models.Model):
    title = models.CharField(max_length=50)
    is_checked = models.BooleanField(default=False)


class Applicant(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.email


class Recruiter(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    head = models.BooleanField(default=False, null=True, blank=True)

    is_confirmed = models.BooleanField(default=False, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.email


class Admin(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.email
