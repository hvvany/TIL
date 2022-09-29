from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
  todo = Todo.objects.order_by('priority')
  context = {
    'todo' : todo,
  }
  return render(request, 'todo/index.html', context)

def create(request):
  content = request.GET.get('content___')
  priority = request.GET.get('priority_')
  deadline = request.GET.get('deadline_')
  Todo.objects.create(content=content, priority=priority, deadline=deadline)
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

def completed(request, todo_pk):
  todo = Todo.objects.get(pk = todo_pk)
  print(todo)
  print(todo.completed)
  if todo.completed == True:
    todo.completed = False
  else:
    todo.completed = True
  todo.save()

  return redirect('todo:index')


def edit(request, todo_pk):
