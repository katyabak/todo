from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import ToDo
from django.contrib.auth.decorators import login_required
from datetime import datetime

def index(request):
    if request.user.is_authenticated:
        # Получаем параметр сортировки из запроса
        sort_by = request.GET.get('sort_by', None)
        # Получаем список всех задач текущего пользователя
        todos = ToDo.objects.filter(user=request.user)
        # Если задан параметр сортировки, сортируем задачи
        if sort_by:
            if sort_by == 'priority':
                todos = sorted(todos, key=lambda todo: ToDo.PRIORITY_ORDER[todo.priority])
            elif sort_by == 'created_at':
                todos = todos.order_by('created_at')
            elif sort_by == 'due_date':
                todos = todos.order_by('due_date')
        return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'Главная страница', 'sort_by': sort_by})
    else:
        return render(request, 'todoapp/index.html', {'title': 'Главная страница', 'user_not_authenticated': True})


@require_http_methods(['POST'])
@csrf_exempt
@login_required
def add(request):
    title = request.POST['title']
    created_at = request.POST['created_at'] if request.POST['created_at'] else datetime.now().date()
    due_date = request.POST['due_date']
    priority = request.POST['priority']
    todo = ToDo.objects.create(title=title, user=request.user, created_at=created_at, due_date=due_date, priority=priority)
    return redirect('index')

@login_required
def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id, user=request.user)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

@login_required
def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id, user=request.user)
    todo.delete()
    return redirect('index')