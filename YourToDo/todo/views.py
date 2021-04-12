from django.shortcuts import render,redirect
from.models import ToDo
from .forms import ToDoForm

def index(request):
    task = ToDo.objects.all() 
    add_task = ToDoForm()
    
    if request.method == 'POST':
        add_task = ToDoForm(request.POST)
        
        if add_task.is_valid():
            add_task.save()
        return redirect ('index')
    else:
        return render(request, 'todo/index.html', {'task':task, 'add_task':add_task})

def delete(request, todo_id):
    del_task = ToDo.objects.get(pk = todo_id)
    del_task.delete()
    return redirect('index')

def edit (request, todo_id):
    task = ToDo.objects.get (pk = todo_id)
    task_form = ToDoForm(instance= task)

    if request.method == 'POST':
        edit_task = ToDoForm(request.POST, instance = task)

        if edit_task.is_valid():
            edit_task.save()
        return redirect ('index')
    
    else:
        return render (request, 'todo/edit.html', {'task' : task, 'task_form': task_form})



