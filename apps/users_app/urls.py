from django.conf.urls import url
from . import views


# TEMPLATE URLS
app_name = 'users_app'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/$', views.register)
]