from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterForm, ComposeForm
from .models import MyUser, Email
from django.conf import settings
import openai

openai.api_key = settings.OPENAI_API_KEY

def index(request):
    if request.user.is_authenticated:
        return redirect('compose')
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('compose')
        else:
            return HttpResponse('Invalid credentials')
    return render(request, 'emailapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'emailapp/register.html', {'form': form})

@login_required
def compose_view(request):
    if request.method == 'POST':
        form = ComposeForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.user = request.user
            email.save()
            return redirect('inbox')
    else:
        form = ComposeForm()
    return render(request, 'emailapp/compose.html', {'form': form})

@login_required
def inbox_view(request):
    emails = Email.objects.filter(user=request.user)
    return render(request, 'emailapp/inbox.html', {'emails': emails})

@login_required
def generate_email_view(request):
    email_content = None
    if request.method == 'POST':
        prompt = request.POST['prompt']
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150
        )
        email_content = response.choices[0].text.strip()
    return render(request, 'emailapp/generate_email.html', {'email_content': email_content})
