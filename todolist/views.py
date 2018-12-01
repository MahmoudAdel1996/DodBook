from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.files.storage import FileSystemStorage


@login_required
def index(request):
    obj = Todo.objects.all()
    context = {
        'todolist': reversed(obj)
    }
    return render(request, 'todolist/index.html', context)


@login_required
def details(request, pk):
    obj = Todo.objects.get(id=pk)
    context = {
        'details': obj
    }
    return render(request, 'todolist/details.html', context)


@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        image = request.FILES.get('image')
        Todo(title=title, text=text, auth=request.user, image=image).save()
        return redirect('index')
    else:
        return render(request, 'todolist/addtodo.html')


@login_required
def delete(request, pk):
    if request.method == 'DELETE':
        Todo.objects.get(id=pk).delete()
        return redirect('index')
    else:
        return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/signup.html', {'form': form, 'error': True})
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    obj = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'registration/profile.html', {'form': form, 'field': obj, 'error': True})
    else:
        form = ProfileForm(instance=request.user)
        return render(request, 'registration/profile.html', {'form': form, 'field': obj})


@login_required
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return render(request, 'registration/chang_pass.html', {'form': form, 'error': True})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'registration/chang_pass.html', {'form': form})


@login_required
def edit_todo(request, pk):
    obj = Todo.objects.get(id=pk)
    if request.user == obj.auth:
        if request.method == 'POST':
            obj.title = request.POST['title']
            obj.text = request.POST['text']
            if request.FILES.get('image'):
                obj.image = None
                obj.image = request.FILES['image']
            obj.save()
            return redirect('index')
        else:
            return render(request, 'todolist/edit_todo.html', {'field': obj})
    else:
        return render(request, 'todolist/404.html')


def errorpage(request):
    return render(request, 'todolist/404.html')