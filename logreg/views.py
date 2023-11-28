from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.
def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.role == 'is_client':
                login(request, user)
                return redirect('client:ClientDashboard')
            elif user is not None and user.role == 'is_admin':
                login(request, user)
                return redirect('dashboard:Dashboard')
            elif user is not None and user.role == 'is_tutor':
                login(request, user)
                return redirect('tutor')
            elif user is not None and user.status == 'not_active':
                login(request, user)
                msg = "Your account has been disabled please contact admin."
                return redirect('login', {'msg': msg})
            else:
                msg = 'Invalid Credentials'
        else:
            msg = 'ERROR VALIDATING FORM'

    return render(request, 'login.html', {'form': form, 'msg': msg})


def client(request):
    return HttpResponse("Client")


def tutor(request):
    return HttpResponse("Tutor")
