from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from django.urls import reverse

from .forms import UserForm


class LoginView(TemplateView, View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        nextPage = request.POST.get('next')
        nextPage = nextPage if nextPage else 'home'
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request, nextPage)
        else:
            messages.warning(request, 'Wrong credentials')
            return redirect(reverse('login'))

class LogoutView(View):
    def post(self, request, *args, **kwargs):
        # TODO: Implement logging out
        messages.warning(request, "Logging out not implemented")
        return redirect('home')


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