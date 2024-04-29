from django.shortcuts import redirect


def role_required(function):
    def wrap(request, *args, **kwargs):
        user = request.user  # getting user object

        if user.is_authenticated:  # if user is logged in
            if user.is_superuser or user.is_staff:  # admin or staff
                return redirect("admin:index")  # redirect to admin panel

            group = user.groups.first()
            if group:
                return redirect(f"{group.name}:index-view")

        return function(request, *args, **kwargs)

    return wrap
