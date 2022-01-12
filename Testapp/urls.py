from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('signup/',views.SignUp,name = 'Signup'),
    path('accounts/signup/learner/',views.LearnerSignUpView.as_view(), name = 'learner_signup')
]