from django.shortcuts import render
from .models import Term
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_only

@login_required(login_url='login')
@admin_only
def terms_index(request):
    terms = Term.objects.all()
    context = {
        'terms': terms
    }
    return render(request, 'term/index.html', context)

# add term view
def term_add(request):
    if request.method == 'POST':
        form = TermAddForm(request.POST)
        context = {
            'form': form
        }
    else:
        form = TermAddForm()
        context = {
            'form': form
        }
        return render(request, 'term/add.html', context)

# edit term view

# delete term view