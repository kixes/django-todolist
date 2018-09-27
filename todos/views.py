from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        try:
            request.POST['completed']
            completed=True
        except:
            completed=False

        todo = Todo(title=title, text=text,completed=completed)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')

def mark_complete(request):
    id = request.POST['id']
    value = request.POST['value']
    Todo.objects.filter(id=id).update(completed=value)
    return redirect('/todos/details/' + id)