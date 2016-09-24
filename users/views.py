from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from .forms import UserForm


class LoginView(TemplateView, View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        nextPage = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if nextPage:
                return redirect(request, nextPage)
            else:
                return redirect('home')
        else:
            messages.warning(request, 'Wrong credentials')
            return redirect('login')

class LogoutView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect('home')
        else:
            return redirect('login')


class RegisterView(TemplateView):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return self.render_to_response({'form': UserForm()})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return self.render_to_response({'form': form})