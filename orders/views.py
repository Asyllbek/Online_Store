from cart.cart import Cart
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            send_mail('Заказ Оформлен',
                      'Войдите в админ панель, что бы просмотреть новый заказ.',
                      'wondroussquirrel@gmail.com',
                      ['alex_zender@i.ua'], fail_silently=False)
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})
