from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from main_app.models import Day, Task


# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('User: ', user.username)
            return HttpResponseRedirect('/profile/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
                else: 
                    print('The account has been disabled.')
                    return render(request, 'login.html', {'form': form})
            else: 
                print('The username and/or password is incorrect.')
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'signup.html', {'form': form})
    else: 
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

class Profile(CreateView):
    model = Task
    fields = ['task', 'description', 'days']
    template_name = "todos.html"
    success_url = "/profile/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        # tasks = Task.objects.filter(user=user)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect("/profile/")

   
class Home(TemplateView):
    template_name = "home.html"

class Days(CreateView):
    model = Day
    fields = ['day', 'tasks']
    def get_form(self):
        form = super().get_form()
        form.fields['day'].widget = DateTimePickerInput()
        return form
        
    template_name = "days.html"
    success_url = "/profile/days"