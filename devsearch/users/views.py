from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm
from .models import Profile


def login_user(request: WSGIRequest):

    page = "login"

    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("profiles")
            else:
                messages.error(request, "Username OR password is incorrect")

    return render(request, "users/login_register.html")


def logout_user(request: WSGIRequest):
    logout(request)
    return redirect("login")


def register_user(request: WSGIRequest):
    page = "register"
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user: User = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created!")

            login(request, user)
            return redirect("profiles")

        else:
            messages.error(request, "An error has occured during registration!")

    context = {"page": page, "form": form}
    return render(request, "users/login_register.html", context)


def profiles(request: WSGIRequest):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)


def user_profile(request: WSGIRequest, pk):
    profile: Profile = Profile.objects.get(id=pk)

    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description__exact="")

    context = {"profile": profile, "topSkills": top_skills, "otherSkills": other_skills}
    return render(request, "users/user-profile.html", context)


@login_required(login_url="login")
def user_account(request: WSGIRequest):
    profile: Profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {"profile": profile, "skills": skills, "projects": projects}
    return render(request, "users/account.html", context)
