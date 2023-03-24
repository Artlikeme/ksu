from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q
from django.contrib.auth.models import Group

from .models import UserProfile
from .forms import NewUserForm


def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        error_ = list(form.errors.values())
        if error_:
            messages.error(request, error_[0])
        if form.is_valid():
            form = form.save()
            login(request, form)
            group = Group.objects.get(name='default')
            request.user.groups.add(group)
            UserProfile.objects.create(fio='Укажите ФИО', phone_num='Укажите номер', user=request.user)
            messages.success(request, "Регистарция произошла успешно")
            return redirect("lk")
        messages.error(request, "Неудачно, данные не корректны")
    form = NewUserForm()
    context = {
        "register_form": form
    }
    return render(request=request, template_name="registration/registr.html", context=context)


def login_reg(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Вы вошли как {username}.")
                return redirect("lk")
            else:
                messages.error(request, "Неверный логин или пароль")
        else:
            messages.error(request, "Неверный логин или пароль")
    form = AuthenticationForm()

    context = {
        "login_form": form,
    }
    return render(request=request, template_name="registration/login.html", context=context)


def logout_request(request):
    logout(request)
    messages.info(request, "Вы успешно вышли из аккаунта")
    return redirect("titlepage")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                messages.success(request, "Correct email, check instruction.")
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        messages.error(request, "Invalid header found. Please, try again")
                        return HttpResponse('Invalid header found.')

                    messages.success(request, "Reset password successful.")
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})
