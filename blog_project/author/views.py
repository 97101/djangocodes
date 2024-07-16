from django.shortcuts import render, redirect
from .forms import authorForm

def add_author(request):
    if request.method == 'POST':
        author_form = authorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("add_author")
    else:
        author_form = authorForm()
    return render(request, 'add_author.html', {'form': author_form})
