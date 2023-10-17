# pip install
# django-admin --version
# python manage.py startapp main
# python manage.py runserver
# python manage.py createsuperuser

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import HomeView, about, shop, ShoppingCardView, checkout, \
    contact, \
    shop_single, \
    thankyou, \
    IncrementCountView, \
    DecrementCountView, AddProductView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', about, name='about'),
    path('shop', shop, name='shop'),
    path('cart', ShoppingCardView.as_view(), name='cart'),
    path('checkout', checkout, name='checkout'),
    path('contact', contact, name='contact'),
    path('thankyou', thankyou, name='thankyou'),
    path('shop_single', shop_single, name='shop_single'),
    path('increment-count', csrf_exempt(IncrementCountView.as_view()), name='increment'),
    path('decrement-count', csrf_exempt(DecrementCountView.as_view()), name='decrement'),
    path('add-product', AddProductView.as_view(), name='add_product'),
]
