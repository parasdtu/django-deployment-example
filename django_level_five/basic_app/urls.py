from django.conf.urls import url
from django.conf.urls import include
from basic_app import views

app_name='basic_app'

urlpatterns=[
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.user_login,name='login'),
]
