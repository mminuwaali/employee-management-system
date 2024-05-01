from django.contrib import messages
from account.forms import ContactForm
from .decorators import role_required
from django.shortcuts import render, redirect


@role_required
def index_view(request):
    return render(request, "landing/index.html")


@role_required
def about_view(request):
    return render(request, "landing/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid() and form.save():
            messages.success(request, "Message sent successfully")
        else:
            messages.error(request, "Message not sent")

        return redirect("landing:contact-view")

    return render(request, "landing/contact.html")
