from django.urls import path
from .views import *

urlpatterns = [
    path("",index, name="index"),
    path("login/",login, name="login"),
    path("logout/",logout, name="logout"),
    path("main_page/",main_page, name="main_page"),
    path('upload/', upload_and_analyze_image, name='upload_and_analyze_image'),

   
]