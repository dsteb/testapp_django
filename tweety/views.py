from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView


class TimelineView(TemplateView, View):
    template_name = 'tweety/home.html'

    def get(self, request, *args, **kwargs):
        # TODO: Implement viewing of the tweets from
        # the users that are being followed
        if not request.user.is_authenticated and not request.GET.get('example'):
            return render(request, template_name='index.html')

        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        # TODO: Implement posting new tweets
        messages.warning(request, "Posting new tweets not implemented")

        return redirect(request.POST.get('next', 'home'))


class ProfileView(TemplateView, View):
    template_name = "tweety/profile.html"

    def get(self, request, *args, **kwargs):
        # TODO: Implement profile pages
        # messages.warning(request, "Profiles not implemented")
        # return redirect('home')
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        # TODO: Implement following/unfollowing users
        pass
