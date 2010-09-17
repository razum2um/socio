# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


from openteam.decorators import render_to
from openteam.shortcuts import redirect_to_view
from openteam.utils import send_email

from forms import SignUpForm, SignInForm

#@render_to("profiles/index.html")
#def index(request):
#    return {}

@render_to("profiles/sign_up.html")
def sign_up(request):
    # catch already authenticated, which try to point their browsers here
    if request.user.is_authenticated(): return redirect_to_view('index')

    sign_up_form = SignUpForm()

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)

        if sign_up_form.is_valid():
            form_data = sign_up_form.cleaned_data
            # check against email address exestance
            email_matching = User.objects.filter(email=form_data['email'])
            if email_matching.count() != 0:
                messages.error(request,
                    u'Email %(email)s уже зарегистрирован. Используйте другой.' %
                    {
                        'email': form_data['email'],
                    }
                )
                return redirect_to_view('sign_up')

            random_password = User.objects.make_random_password()

            User.objects.create_user(
                username = form_data['email'],
                email    = form_data['email'],
                password = random_password,
            )
            # Send newly created user its password throug email
            send_email(
                to = form_data['email'],
                tpl = 'signup',
                context = {
                    'email': form_data['email'],
                    'password': random_password,
                }
            )
            # Authenticate user on site, to omit usless step of viewing email and
            # filling form with login/pass
            user = authenticate(
                username = form_data['email'],
                password = random_password
            )
            login(request, user)
            # Greetings for newly signed up user
            messages.success(request, u"""Поздравляем вас! Теперь Вы &mdash;
                пользователь сайта. Мы уже сделали за вас вход на сайт.
                Надеемся, этот визит не станет последним. Для этого вам на
                электронную почту был отправлен пароль для входа на сайт."""
            )

            return redirect_to_view('index')

    return {
            'sign_up_form': sign_up_form,
        }

@login_required
def sign_out(request):
    logout(request)

    return redirect_to_view('index')

@render_to("profiles/show.html")
def show(request, id):
    user = get_object_or_404(User, id=id)
    return {
        'user': user,
    }

#@render_to("profiles/edit.html")
#def edit(request, id):
#    return {}

#@render_to("profiles/block.html")
#def block(request, id):
#    return {}

#@render_to("profiles/delete.html")
#def delete(request, id):
#    return {}

