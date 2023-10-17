from django.db.models import Q

from .models import ShoppingCard

def increment_count(id, user): # noqa
    try:
        shopping_cart = ShoppingCard.objects.get(Q(product_id=id) & Q(user=user))
        shopping_cart.count += 1
        shopping_cart.save()
    except: # noqa
        return False
    return True

def decrement_count(id, user): # noqa
    try:
        shopping_cart = ShoppingCard.objects.get(Q(product_id=id) & Q(user=user))
        shopping_cart.count -= 1
        shopping_cart.save()
    except: # noqa
        return False
    return True # noqa








