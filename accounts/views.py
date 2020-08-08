from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile, Lesson
from .forms import LoginForm, TeacherEditForm, LessonForm
from django.contrib import messages

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

def teacher_edit(request, pk):
    user = User.objects.get(id=pk)
    profile = UserProfile.objects.get(user=pk)
    form = TeacherEditForm(request.POST or None, instance=profile)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(f'/account/teachers/{pk}')
    else:             
        context = {
            'form': form,
            'user': user
        }
        return render(request, 'accounts/teacher_edit.html', context)

def lesson_add(request, pk):
    form_user = User.objects.get(id=pk)
    form = LessonForm(request.POST or None)
    if request.method == "POST":
        print(form.is_valid())
        if form.is_valid():
            cd = form.cleaned_data
            new = Lesson(
                user=form_user,
                course_title=cd['course_title'],
                grade=cd['grade'],
                lesson_title=cd['lesson_title'],
                theorical_unit=cd['theorical_unit'],
                practical_unit=cd['practical_unit'],
                theorical_time=cd['theorical_time'],
                practical_time=cd['practical_time'],
                group=cd['group']
            )
            new.save()
            return redirect(f'/account/teachers/{pk}') 
    else:
        context = {
            'form': form
        }
        return render(request, 'accounts/add_lesson.html', context)

def lesson_edit(request, pk):
    lesson = Lesson.objects.get(id=pk)
    form = LessonForm(request.POST or None, instance=lesson)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(f'/account/teachers/{lesson.user_id}')
    else:
        context = {
            'form': form
        }
        return render(request, 'accounts/edit_lesson.html', context)