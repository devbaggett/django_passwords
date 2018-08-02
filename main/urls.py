from django.contrib import admin
from django.conf.urls import url, include
from apps.users_app import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^users_app/', include('apps.users_app.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/', views.special, name='special'),
]