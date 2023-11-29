from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages


# Create your views here.
def dashboard(request):
    task = Task.objects.filter(status='Pending')
    task_count = Task.objects.count()
    pending_task = Task.objects.filter(status='Pending').count
    completed_task = Task.objects.filter(status='Closed').count
    return render(request, 'clientdash.html', {'navbar': 'clientdash', 'task': task, 'task_count': task_count, 'pending_task': pending_task, 'completed_task': completed_task})


def addTask(request):
    task = Task.objects.all()
    return render(request, 'add_task.html', {'navbar': 'addtask', 'task': task})


def taskHistory(request):
    task = Task.objects.all()
    return render(request, 'task_history.html', {'navbar': 'taskHistory', 'task': task})


def myTask(request):
    task = Task.objects.all()
    return render(request, 'my_task.html', {'navbar': 'myTask', 'task': task})


def addNewTask(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        course = request.POST.get('course')
        budget = request.POST.get('budget')
        deadline = request.POST.get('deadline')
        uploaded_by = request.POST.get('uploaded_by')
        status = "Pending"
        bid_by = 0
        approval = "Pending"
        submission = "Pending"
        payment = "Pending"

        if len(request.FILES) != 0:
            document = request.FILES['document']

        query = Task(title=title, description=description, course=course, budget=budget, deadline=deadline,
                     status=status, document=document, uploaded_by=uploaded_by, bid_by=bid_by, approval=approval, submission=submission, payment=payment)
        query.save()
        messages.success(request, 'Team Member added successfully!')
        return redirect("/client/addTask")
    return redirect("/client/addTask")
