# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from openteam.decorators import render_to
from openteam.shortcuts import redirect_to_view
from profiles.forms import SignUpForm

@render_to("profiles/sign_up.html")
def sign_up(request):

    if request.user.is_authenticated():
        return redirect_to_view('index')

    sign_up_form = SignUpForm(request.POST or None)

    if sign_up_form.is_valid():
        form_data = sign_up_form.cleaned_data
        email_matching = User.objects.filter(email=form_data['email'])

        if email_matching.count():
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
        send_email(to=form_data['email'], tpl='signup',
                   context = {
                    'email': form_data['email'],
                    'password': random_password,
                    }
        )
        user = authenticate(username=form_data['email'], password=random_password)

        UserProfile.objects.create(user=user)

        login(request, user)

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

