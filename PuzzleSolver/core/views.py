from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            request.session['initial_state'] = form.cleaned_data['initial_state']
            request.session['search_algorithm'] = form.cleaned_data['search_algorithm']
            #redirect
    return render(request, 'home.html', {'form': form})

def solve(request):

    context = {

    }
    return render(request, 'home.html', context)
