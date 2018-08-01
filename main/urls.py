from django.contrib import admin
from django.conf.urls import url, include
from apps.users_app import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^users_app/', include('apps.users_app.urls')),
]
