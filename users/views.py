from django.shortcuts import render,redirect
from .forms import NewUserForm , LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm

from django.http import Http404

# Create your views here.
def register_request(request):
    if request.method == "POST":
	    form = NewUserForm(request.POST)
	    if form.is_valid():
		    user = form.save()
		    login(request, user)
		    messages.success(request, "Registration successful." )
		    return redirect("home")
	    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


def login(req):
    form = UserSigninForm()
    if req.method == "POST":
        form = UserSigninForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect("home")
    context = {"form": form }
    return render(req, "login.html", context)







def login_request(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)

            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("home/")

    context = {
        "LoginForm": form,
    }
    return render(request, "login.html", context)


def logout_request(request):
    logout(request)
    
    messages.info(request,"you have successfully logged out")
    return redirect("login")

def permission(request):
    if request.user.is_anonymous:
        return redirect("login")
    elif not request.user.is_staff:
        raise Http404


                


