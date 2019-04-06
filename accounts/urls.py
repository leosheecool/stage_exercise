from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^create/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.profile_editor1, name='profile_editor'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'})
]