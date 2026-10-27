from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task

# Create your views here.

@login_required
def index(request):
    tasks = Task.objects.filter(owner=request.user)
    status = request.GET.get('status', 'all')
    search = request.GET.get('search')

    count_total_tasks= tasks.count()
    count_completed = 0
    count_pending= 0
    filter_data_found = True
    
    for task in tasks:
        if task.is_completed:
            count_completed += 1
        else:
            count_pending += 1

    if status == 'pending':
        tasks = tasks.filter(is_completed=False)
        if not tasks:
            filter_data_found = False

    elif status == 'completed':
        tasks = tasks.filter(is_completed=True)
        if not tasks:
            filter_data_found = False

    if tasks:
        if search:
            tasks = tasks.filter(title__icontains=search)
    
    search_not_found = bool(search and not tasks.exists())

    
    return render(request, "todo/index.html",{
        "tasks":tasks,
        "total":count_total_tasks,
        "completed":count_completed,
        "pending": count_pending,
        "selected_status": status,
        "search":search,
        "search_not_found":search_not_found,
        "filter_data_found": filter_data_found,
    })



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        next_url = request.POST.get("next") or request.GET.get("next")

        if user is not None:
            login(request, user)

            if next_url:
                return redirect(next_url)
            return redirect("index")

        return render(
            request, 
            "todo/login.html",
            {"error": "Invalid username or password"}
        )

    return render(request, "todo/login.html")
    
def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Password do not match!")
            return render(request, "todo/signup.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, "todo/signup.html")

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )

        messages.success(request, "Signup successful! Please login.")

        return redirect("login")

    return render(request, "todo/signup.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def add_task(request):
    print("faH")
    if request.method == "POST":
        print("add")
        title=request.POST.get("title")

        Task.objects.create(
            title=title,
            owner=request.user
        )

    return redirect("index")
    

@login_required
def update_task_view(request, task_id):
    if request.method == "POST":
        update_title = request.POST.get("update_title")

        if update_title:
            task = get_object_or_404(
                Task,
                id=task_id,
                owner=request.user
            )

            task.title = update_title

            task.save()

    return redirect("index")

@login_required
def iscompleted(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(
            Task,
            id=task_id,
            owner=request.user
        )

        task.is_completed = not task.is_completed

        task.save()
    return redirect("index")

def delete_view(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(
            Task, 
            id=task_id,
            owner=request.user
        )

        task.delete()
    return redirect("index")

def helpview(request):
    return render(request, "todo/help.html")