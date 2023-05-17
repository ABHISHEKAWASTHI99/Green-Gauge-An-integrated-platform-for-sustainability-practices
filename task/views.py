from django.shortcuts import render, redirect
from .models import Challenge, TaskCategory, User_Task
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def task(request):
    challenges = Challenge.objects.all()
    categories = TaskCategory.objects.all()
    # count challenges per category
    for category in categories:
        category.challenge_count = Challenge.objects.filter(category=category).count()
    user_tasks = User_Task.objects.all()
    context = {
        'challenges': challenges,
        'categories': categories,
        'user_tasks': user_tasks
    }
    return render(request, 'task/task.html', context)

@login_required
def complete_task(request, id):
    challenge = Challenge.objects.get(pk=id)
    user_task = User_Task(
        user=request.user,
        challenge=challenge,
        completed=True
    )
    user_task.save()
    messages.success(request, 'Congratulations! You have completed the challenge.')
    return redirect('tasks')
@login_required
def challenge_detail(request, pk):
    challenge = Challenge.objects.get(pk=pk)
    user_task = User_Task.objects.filter(user=request.user, challenge=challenge).first()
    context = {
        'challenge': challenge,
        'user_task': user_task,
    }
    return render(request, 'task/challenge_detail.html', context)


@login_required
def report(request):
    user_tasks = User_Task.objects.filter(user=request.user)
    total_tasks = user_tasks.count()
    score_per_task = 100
    total_score = 0
    for task in user_tasks:
        if task.completed:
            total_score += score_per_task
    
    context = {
        'user_tasks': user_tasks,
        'total_score': total_score,
        'total_tasks': total_tasks,
    }
    return render(request, 'task/report.html', context)