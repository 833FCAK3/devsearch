from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from .models import Profile


# Create your views here.


def profiles(request: WSGIRequest):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)


def userProfile(request: WSGIRequest, pk):
    profile: Profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description__exact="")

    context = {"profile": profile, "topSkills": topSkills, "otherSkills": otherSkills}
    return render(request, "users/user-profile.html", context)
