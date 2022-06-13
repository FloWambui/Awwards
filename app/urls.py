from django.urls import re_path
from . import views

app_name = "app" 


urlpatterns=[
    re_path('^$',views.home,name = 'homepage'),
    re_path("register", views.register_request, name="register")
]