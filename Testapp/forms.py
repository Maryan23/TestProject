from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *

class LearnerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(max_length=10,required=True)
    email = forms.EmailField(required=True)
    tel_number = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        learner = Learner.objects.create(user=user)
        learner.first_name = self.cleaned_data.get('first_name')
        learner.last_name = self.cleaned_data.get('last_name')
        return learner

class MentorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    second_name = forms.CharField(max_length=10,required=True)
    email = forms.EmailField(required=True)
    tel_number = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_mentor = True
        user.save()
        mentor = Mentor.objects.create(user=user)
        mentor.first_name = self.cleaned_data.get('first_name')
        mentor.second_name = self.cleaned_data.get('last_name')
        mentor.tel_number = self.cleaned_data.get('tel_number')
        mentor.staff_number = self.cleaned_data.get('stuff_number')
        mentor.save()

        return mentor