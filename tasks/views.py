from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import SignUpForm, TaskForm
from .models import Task

def signup(request):
    if request.user.is_authenticated:
        return redirect("task_list")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome! Your account has been created.")
            return redirect("task_list")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def task_list(request):
    # Filter on the server so users only ever see their own tasks.
    tasks = Task.objects.filter(user=request.user)
    total_count = tasks.count()
    completed_count = tasks.filter(is_completed=True).count()
    pending_count = total_count - completed_count
    return render(request, "tasks/task_list.html", {
        "tasks": tasks,
        "total_count": total_count,
        "completed_count": completed_count,
        "pending_count": pending_count,
    })

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task added successfully.")
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, "page_title": "Add a task"})

@login_required
def task_update(request, pk):
    # Include the current user in the lookup to prevent cross-user edits.
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form, "page_title": "Edit task"})

@login_required
def task_toggle(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.is_completed = not task.is_completed
        task.save(update_fields=["is_completed"])
        messages.success(request, "Task status updated.")
    return redirect("task_list")

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted.")
        return redirect("task_list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})
