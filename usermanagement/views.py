from django.shortcuts import render,redirect
from .models import Flower,Cart,Order
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def shopview(request):
    flowers = Flower.objects.all()
    return render(request,"shop.html",{'flowers':flowers})
def cartview(request):
    items = Cart.objects.filter(user=request.user)
    total=0
    for item in items:
        if item.flower.is_on_sale:
            total =total + item.flower.sale_price * item.quantity
        else:
            total =total + item.flower.price * item.quantity
    
    return render(request,"cart.html" ,{'items':items,'total':total})

def add_to_cart(request,pk):
    flowers=Flower.objects.get(id=pk)
    items, created = Cart.objects.get_or_create(flower=flowers, user=request.user)
    enteredQuantity = request.POST['quantity']
    items.quantity= enteredQuantity
    items.save()
    messages.add_message(request,messages.SUCCESS,"Successfully Added To Cart")
    return redirect('/user/cart/')

def del_from_cart(request,pk):
    items=Cart.objects.get(id=pk)
    items.delete()
    return redirect('/user/cart/')


# tera lotus bohot mehenga hai re 
# hai kay kel mala nai samjhl
# samjha kuch?hn samjha toh aise hota hai data pass django me, form tag banao aur post request maarke usme data dedo toh request.POST ke andar name attribute se mil jata
# form ke andar jitne bhi input hote hai, sabka value post request me chala jata hai django ke paas
# ab django ko kaise pata chalta hai ki value kaise nikaalni hai? name attribute se
# usko request object me post ke andar name attribute se uska value milgya woh uthake maine tere quantity ko dedia

def order(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)

        if cart_items.exists():
            phone = request.POST['phone']
            address = request.POST['address']
            cart_data = {}
            for item in cart_items:
                cart_data[item.flower.id] = {
                    'name': item.flower.name,
                    'quantity': item.quantity,
                }
            orders = Order.objects.create(
                user=request.user,
                phone=phone,
                address=address,
                status='pending',
                cart=cart_data,
            )

            cart_items.delete()
            send_mail(
            subject='Welcome to Our Bloomy!',
            message=f'Hello {request.user.username}, Your Order Place Succssefully!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email],
            fail_silently=False,
            )
            messages.success(request, "Order placed successfully!")
            return redirect('/user/bill/')
            
    return render(request,'cart.html')

def bill(request):
    orders = Order.objects.filter(user=request.user).order_by('-id').first()
    return render(request, 'bill.html', {'orders': [orders]})
   
    