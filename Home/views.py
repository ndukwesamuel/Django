from django.shortcuts import render

# Create your views here.

from Home.models import TodoData


def home(request):
    todos = TodoData.objects.all()
    context ={
        'todolist':todos
    }


    return render( request, 'index.html', context)

def todo_detail(request, id):

    todo = TodoData.objects.get(id=id)

    context = {
        'todo':todo
    }

    return render(request, 'detail.html', context)
