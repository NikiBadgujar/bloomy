

from django.urls import path
from . import views 
urlpatterns = [
    
    path('',views.homeview,name='home'),
    path('about/',views.aboutview,name='about'),
    path('contact/',views.contactview,name='contact'),
    
] 
