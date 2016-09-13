from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.TimelineView.as_view(),
        name='home'
    ),

    url(
        regex=r'^profile/(?P<id>[0-9]+)/$',
        view=views.ProfileView.as_view(),
        name='profile'
    ),
]
