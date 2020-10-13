from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile, Lesson, Lessonaccepted
from .forms import LoginForm, TeacherEditForm, LessonForm, SignForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only

@login_required(login_url='login')
@admin_only
def index(request):
    return render(request, 'accounts/index.html')

@login_required(login_url='login')
def teacher_index(request):
    lessons = Lesson.objects.filter(user=request.user)
    theo_total_unit = 0
    prac_total_unit = 0
    theo_total_time = 0
    prac_total_time = 0
    total_group = 0
    for lesson in lessons:
        # if lesson.lessonaccepted.exists():
        if Lessonaccepted.objects.filter(lesson=lesson).exists():
            theo_total_unit += (lesson.theorical_unit * lesson.group)
            prac_total_unit += (lesson.practical_unit * lesson.group)
            theo_total_time += (lesson.theorical_time * lesson.group)
            prac_total_time += (lesson.practical_time * lesson.group)
            total_group += lesson.group

    context = { 
        'lessons': lessons,
        'theo_total_unit': theo_total_unit,
        'prac_total_unit': prac_total_unit,
        'theo_total_time': theo_total_time,
        'prac_total_time': prac_total_time,
        'total_group': total_group
   }
    return render(request, 'accounts/teacher_index.html', context)

@unauthenticated_user
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
                return redirect('/account')
    else:
        form = LoginForm()
        context = {
            'form': form
            }
        return render(request, 'accounts/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def teachers_list(request):
    teachers = User.objects.all
    return render(request, 'accounts/teachers_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = User.objects.get(id=pk)
    lessons = Lesson.objects.filter(user=pk)
    context = {
        'teacher': teacher,
        'lessons': lessons,
    }
    return render(request, 'accounts/teacher_detail.html', context)

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

def print_tuition(request, pk):
    lessons = Lesson.objects.filter(user=pk)
    teacher = User.objects.get(id=pk)
    theo_total_unit = 0
    prac_total_unit = 0
    theo_total_time = 0
    prac_total_time = 0
    total_group = 0
    for lesson in lessons:
        if Lessonaccepted.objects.filter(lesson=lesson).exists():
            theo_total_unit += (lesson.theorical_unit * lesson.group)
            prac_total_unit += (lesson.practical_unit * lesson.group)
            theo_total_time += (lesson.theorical_time * lesson.group)
            prac_total_time += (lesson.practical_time * lesson.group)
            total_group += lesson.group
    context = {
        'teacher': teacher,
        'lessons': lessons,
        'theo_total_unit': theo_total_unit,
        'prac_total_unit': prac_total_unit,
        'theo_total_time': theo_total_time,
        'prac_total_time': prac_total_time,
        'total_group': total_group
    }
    return render(request, 'accounts/print_tuition.html', context)

def teacher_sign(request):
    profile = UserProfile.objects.get(user=request.user)
    form = SignForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('/account')
    context = {
        'form': form
    }
    return render(request, 'accounts/teacher_sign.html', context)

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

def lesson_accept(request, pk):
    lesson = Lesson.objects.get(id=pk) 
    theorical_total = lesson.theorical_time * request.user.userprofile.theorical_pay
    practical_total = lesson.practical_time * request.user.userprofile.practical_pay
    total = theorical_total + practical_total
    if request.method == 'POST':
        if Lessonaccepted.objects.filter(lesson_id=pk).exists():
            return redirect('/account/home')
        else:
            if request.POST.get('accept'):
                acc = Lessonaccepted(user=request.user, lesson=lesson)
                acc.save()
                return redirect('/account/home')
            else:
                return redirect('/account/home')
    else:       
        context = {
            'lesson': lesson,
            'theorical_total': theorical_total,
            'practical_total': practical_total,
            'total': total
        }
        return render(request, 'accounts/lesson_accept.html', context)