from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# random_word = get_random_string(length=14) 

def random_word(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    request.session['attempts'] += 1
    request.session['word'] = get_random_string(length=14)
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')