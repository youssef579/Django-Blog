from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.user.is_authenticated:
        messages.warning(request, "You have to log out to be able to register")
        return redirect("home")
    
    match request.method:
        case "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account has been created. You can log in now.')
                return redirect('login')
        case _:
            form = RegisterForm()

    return render(request, "authentication/register.html", {"form": form})