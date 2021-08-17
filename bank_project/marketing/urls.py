from django.urls import path, include
# add this to import our views file
from django.contrib.auth import views as auth_view
from .import views

app_name = "marketing" 

urlpatterns = [
    path('', views.index, name='home'),
    path('result/', views.result, name='result'),
    path("account/", include("django.contrib.auth.urls"), name='login'),
    path("signup/", views.register, name="signup"),
    # path("login/", auth_view.LoginView.as_view(template_name= "registration/login.html"), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name= "registration/logout.html"), name = "logout"),
]
    

