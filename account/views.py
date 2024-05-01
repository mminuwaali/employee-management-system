from . import forms, models
from django.db.models import Q
from landing.models import Course
from student.forms import EnrollmentForm
from django.contrib import auth, messages
from django.shortcuts import render, redirect


def signout_view(request):
    auth.logout(request)
    return redirect(request.GET.get("next", "/"))


def signup_view(request):
    if request.method == "POST":
        if models.User.objects.filter(
            Q(email=request.POST.get("email"))
            | Q(username=request.POST.get("username"))
        ).exists():
            messages.warning(
                request, "A user with the same email or username already exists"
            )
        form = EnrollmentForm(request.POST)

        if form.is_valid() and form.save():
            messages.success(request, "You have succes requested for enrollment")
            messages.success(request, "Keep an eye for an email update")
            return redirect("account:signin-view")

        [messages.error(request, i[0]) for i in form.errors.values()]
        return redirect("account:signup-view")

    courses = Course.objects.all()

    context = {"courses": courses}
    return render(request, "account/signup.html", context)


def signin_view(request):
    if request.method == "POST":
        user = auth.authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )

        if user and user.groups.count():
            auth.login(request, user)
            return redirect("landing:index-view")

        messages.error(request, "Invalid credentials")
        return redirect("account:signin-view")

    return render(request, "account/signin.html")
