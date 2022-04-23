from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic.edit import View, CreateView, UpdateView, DeleteView
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

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

class Task_Delete(DeleteView):
        model = Task
        template_name = "task_delete.html"
        success_url = "/profile/"

class Task_Update(UpdateView):
    model = Task
    fields = ['task', 'description', 'is_complete']
    template_name = "task_update.html"
    success_url = "/profile/"    

class Home(TemplateView):
    template_name = "home.html"

class Days(CreateView):
    model = Day
    fields = ['day']
    template_name = "days.html"
    success_url = "/profile/days"

    def get_form(self):
        form = super().get_form()
        form.fields['day'].widget = DatePickerInput()
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect("/profile/days")
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["days"] = Day.objects.all()
        # tasks = Task.objects.filter(user=user)
        return context