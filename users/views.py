from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from .forms import UserForm


class LoginView(TemplateView, View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        # TODO: Implement logging in
        messages.warning(request, "Logging in not implemented")

        return redirect(request.POST.get('next', 'home'))


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
            return redirect('home')
        else:
            return self.render_to_response({'form': form})