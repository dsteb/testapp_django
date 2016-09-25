from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from users.models import UserProfile

from .models import Tweet


class TimelineView(TemplateView, View):
    template_name = 'tweety/home.html'

    def get(self, request, *args, **kwargs):
        # TODO: Implement viewing of the tweets from
        # the users that are being followed
        if not request.user.is_authenticated and not request.GET.get('example'):
            return render(request, template_name='index.html')

        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            message = request.POST['message']
            tweet = Tweet(profile=request.user.userprofile, message=message, pub_datetime=timezone.now())
            tweet.save()
            return redirect('home')


class ProfileView(LoginRequiredMixin, TemplateView, View):
    template_name = "tweety/profile.html"

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(UserProfile, pk=kwargs['id'])
        latest_tweets = profile.tweet_set.all()[:10]
        return self.render_to_response({
            'latest_tweets': latest_tweets,
            'profile_user': profile.user,
            'follows': request.user.userprofile.is_following(profile.user.id)
        })

    def post(self, request, *args, **kwargs):
        pk = kwargs['id']
        unfollow = request.user.userprofile.follows.filter(pk=pk).exists()
        if unfollow:
            request.user.userprofile.follows.remove(pk)
        else:
            request.user.userprofile.follows.add(pk)
        return redirect(request.path)