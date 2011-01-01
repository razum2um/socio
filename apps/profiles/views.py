# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from openteam.decorators import render_to
from openteam.shortcuts import redirect_to_view, get_object_or_none
from openteam.utils import send_email

from forms import SignUpForm, UserForm, UserProfileForm
from models import UserProfile

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
    owner = get_object_or_404(User, id=id)

    if get_object_or_none(UserProfile, user=owner) is None:
        UserProfile.objects.create(user=owner)

    return dict(
        owner = owner,
        current_page = dict(
           title = u'Профиль',
            slug = 'dossier'
        ),
    )

@render_to("profiles/photos.html")
def photos(request, id):
    return {}


@login_required
@render_to("profiles/edit.html")
def edit(request, id):
    owner = get_object_or_404(User, id=id)

    if request.user.id != owner.id and request.user.is_superuser == False:
        return redirect_to_view('index')

    profile = owner.get_profile()
    user_form = UserForm(request.POST or None, instance=owner, prefix='user_')
    profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile, prefix='profile_')

    if user_form.is_valid():
        user_form.save()

    if profile_form.is_valid():
        profile_form.save()

    return {
        'profile_form': profile_form,
        'user_form': user_form,
        'owner': owner,
    }

#@render_to("profiles/block.html")
#def block(request, id):
#    return {}

#@render_to("profiles/delete.html")
#def delete(request, id):
#    return {}

@render_to('profiles/dashboard.html')
def dashboard (request):
    return dict()

