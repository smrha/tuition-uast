from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project

def index(request):
    context = {}
    return render(request, 'worksheet/index.html', context)

def project_add(request):
    pass
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            p = Project(
                teacher = request.user, first_name = cd['first_name'], last_name = cd['last_name'],
                std_id = cd['std_id'], n_id = cd['n_id'], field = cd['field'], degree = cd ['degree'],
                start_date = cd['start_date'], end_date = cd['end_date'], score = cd['score'],
                score_letters = cd['score_letters'],
                value_question1 = cd['value_question1'], value_question2 = cd['value_question2'],
                value_question3 = cd['value_question3'], value_question4 = cd['value_question4'],
                desc_question1 = cd['value_question1'], desc_question2 = cd['value_question2'],
                desc_question3 = cd['value_question3'], desc_question4 = cd['value_question4'],
            ) 
            p.save()
            return HttpResponse('فرم با موفقیت ثبت گردید')
            # cd = form.cleaned_data
    #         p = Project(
    #             teacher = request.user,
    #             first_name = cd['first_name'],
    #             last_name = cd['last_name'],
    #             std_id = cd['std_id'],
    #             n_id = cd['n_id'],
    #             field = cd['field'],
    #             degree = cd ['degree'],
    #             start_date = cd['start_date'],
    #             end_date = cd['end_date'],
    #             score = cd['score'],
    #             score_letters = cd['score_letters'] ,
    #         )        
    #         p.save()
    #         q1 = ProjectQuestion(
    #             proj = p,
    #             question = QuestionType.objects.get(id=1),
    #             value = cd['question_value1'],
    #             description = cd['question_desc1'],
    #         )
    #         q1 = ProjectQuestion(proj = p, question = QuestionType.objects.get(id=1),
    #                 value = cd['question_value1'], description = cd['question_desc1'])
    #         q2 = ProjectQuestion(proj = p, question = QuestionType.objects.get(id=2),
    #                 value = cd['question_value2'], description = cd['question_desc2'])
    #         q3 = ProjectQuestion(proj = p, question = QuestionType.objects.get(id=3),
    #                 value = cd['question_value3'], description = cd['question_desc3'])
    #         q4 = ProjectQuestion(proj = p, question = QuestionType.objects.get(id=4),
    #                 value = cd['question_value4'], description = cd['question_desc4'])
    #         q1.save()
    #         q2.save()
    #         q3.save()
    #         q4.save()
    #         return redirect('project_list')
    #     else:
    #         return HttpResponse('مشکلی در ثبت داده ها بوجد آمده لطفا با مدیر سیستم تماس بگیرید.')
    else:
        data = {'teacher': request.user}
        form = ProjectForm(initial=data)
        
    #     question_type1 = QuestionType.objects.get(id=1)
    #     question_type2 = QuestionType.objects.get(id=2)
    #     question_type3 = QuestionType.objects.get(id=3)
    #     question_type4 = QuestionType.objects.get(id=4)
        context = {
            'form': form,
    #         'question_type1': question_type1,
    #         'question_type2': question_type2,
    #         'question_type3': question_type3,
    #         'question_type4': question_type4,
        }
        return render(request, 'worksheet/project_add.html', context)

def project_list(request):
    if request.user.groups.all()[0].name == 'expert':
        projects = Project.objects.all()
        context = { 
            'projects': projects
        }
        return render(request, 'worksheet/project_list.html', context)
    else:
        projects = Project.objects.filter(teacher=request.user)   
        context = { 
            'projects': projects
        }
        return render(request, 'worksheet/project_list.html', context)

def project_show(request, pk):
    p = Project.objects.get(id=pk)
    # ProjectQuestion.objects.filter(id=)