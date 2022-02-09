import logging
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

from users.forms import SignUpForm

logger = logging.getLogger("news_authenticity")


class LoginView(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, "users/login.html", context={"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.data.get("username")
            password = form.data.get("password")
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect("/news")

        else:
            return render(request, "users/login.html", context={"form": form})


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/news")
        return render(request, 'users/signup.html', {'form': form})
