from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Lesson
from .forms import LoginForm

def index(request):
    return render(request, 'accounts/index.html')

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])    
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account.')
            else:
                return HttpResponse('Invalid login.')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

def teachers_list(request):
    teachers = User.objects.all
    return render(request, 'accounts/teachers_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = User.objects.get(id=pk)
    lessons = Lesson.objects.filter(user=pk)
    return render(request, 'accounts/teacher_detail.html', {'teacher': teacher, 'lessons': lessons})