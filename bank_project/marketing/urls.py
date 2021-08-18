from django.urls import path, include
# add this to import our views file
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('result/', views.result, name='result'),
    path("account/", include("django.contrib.auth.urls")),
    path("signup/", views.SignUp.as_view(), name = "signup"),
    path("logout/", views.logout_request, name= "logout"),
]
    

