from django.urls import re_path
from . import views

app_name = "app" 


urlpatterns=[
    re_path('^$',views.home,name = 'homepage'),
    re_path("register", views.register_request, name="register"),
    re_path("login", views.login_request, name="login"),
    re_path("logout", views.logout_request, name= "logout"),
    re_path('profile/',views.profile, name='profile'),
    re_path('updateprofile/', views.update_profile, name='update_profile'),
    re_path('upload/',views.post_project,name='post_prj'),
    re_path('project_info/(?P<id>\d+)', views.view_project, name='viewProject'),
    re_path('search/', views.search, name='search'),

]