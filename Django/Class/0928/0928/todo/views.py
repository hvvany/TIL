from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
  todo = Todo.objects.all()
  context = {
    'todo' : todo,
  }
  return render(request, 'todo/index.html', context)

def create(request):
  content = request.GET.get('content___')
  Todo.objects.create(content=content)
  # todo = Todo.objects.all()
  # context = {
  #   'todo' : todo,
  # }

  # return render(request, 'todo/index.html',context)
  return redirect('todo:index')

def delete(request, todo_pk):
  todo = Todo.objects.get(pk = todo_pk)
  todo.delete()

  return redirect('todo:index')