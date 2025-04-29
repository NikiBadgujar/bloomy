from django.contrib import admin
from django.core.mail import send_mail
from .models import Flower, Cart, Order
import random
from django.conf import settings

admin.site.register(Flower)
admin.site.register(Cart)
# custom model for orders
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'phone', 'address')
    list_editable = ('status',)

    def save_model(self, request, obj, form, change):
        if change:
            old = Order.objects.get(id=obj.id)
            if old.status != obj.status:
                if obj.status == "Dispatched":
                    otp = str(random.randint(100000, 999999))
                    obj.otp = otp
                    send_mail(
                        subject="Your Order is Dispatched – Delivery OTP Inside",
                        message=(
                            f"Hi {obj.user.username},\n\n"
                            f"Your order has been dispatched.\n"
                            f"Use this OTP to confirm delivery: {otp}\n\n"
                            f"Thank you for shopping with Bloomy!"
                        ),
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[obj.user.email],
                        fail_silently=False
                    )
                elif obj.status == "delivered":
                    send_mail(
                        subject="Order Delivered",
                        message=(
                            f"Hi {obj.user.username},\n\n"
                            f"Your order has been delivered successfully.\n\n"
                            f"Thanks for shopping with us!"
                        ),
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[obj.user.email],
                        fail_silently=False
                    )
        super().save_model(request, obj, form, change)
