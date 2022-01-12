from django.shortcuts import redirect, render
from .forms import LearnerSignUpForm,MentorSignUpForm
from .models import *
from django.contrib.auth import login
from django.views.generic import CreateView

# Create your views here.
def index(request):    
    current_user = request.user
    return render(request,'index.html')

def SignUp(request):
    return render(request,'register.html')

class LearnerSignUpView(CreateView):
    model = User
    form_class = LearnerSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'learner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('index')

class MentorSignUpView(CreateView):
    model = User
    form_class =MentorSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'mentor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')