from django.shortcuts import render, redirect
from .models import Term
from .forms import TermAddForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_only
from datetime import datetime
from khayyam import JalaliDate

@login_required(login_url='login')
@admin_only
def terms_index(request):
    terms = Term.objects.all()
    context = {
        'terms': terms
    }
    return render(request, 'term/index.html', context)

def term_add(request):
    if request.method == 'POST':
        form = TermAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('terms_index')
        else:
            form = TermAddForm()
            context = {
                'form': form
            }
            return render(request, 'term/add.html', context)
    else:
        form = TermAddForm()
        context = {
            'form': form
        }
        return render(request, 'term/add.html', context)

# edit term view

# delete term view

# active term view

# deactive term view