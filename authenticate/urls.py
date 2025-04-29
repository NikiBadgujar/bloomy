
from django.urls import path
from . import views 
urlpatterns = [
    path('login/',views.loginuser),
    path('signup/',views.signupuser),
    path('logout/',views.logoutuser),
    
] 
