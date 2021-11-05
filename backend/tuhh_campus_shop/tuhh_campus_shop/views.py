from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register_request(request): #Julius
    if request.method == "POST":
        form = NewUserForm(request.post)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect("main:homepage")
        messages.error(request, "Registration was not successfull")
        form = NewUserForm
        #return zu registrierungsseite nochmal

def login_request(request): #julius
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info("login successfull")
                return redirect('main:homepage')
            else:
                messages.error(request, "login was not successfull, \ninvalid username or password.")
        form = AuthenticationForm()