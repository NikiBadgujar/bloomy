

from django.urls import path,include
from . import views 
urlpatterns = [
    
    path('shop/',views.shopview),
    path('cart/',views.cartview),
    path('add/<int:pk>',views.add_to_cart,name='add_item'),
    path('delete/<int:pk>',views.del_from_cart,name='del_item'),
    path('order/',views.order),
    path('bill/',views.bill),
    
    
] 
