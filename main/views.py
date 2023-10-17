import json

from django.views import View
from .forms import ProductForm
from django.db.models import Q
from .models import ShoppingCard
from django.contrib import messages
from django.http import JsonResponse
from main.models import Product, Picture
from .utils import increment_count, decrement_count
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView


class HomeView(View):  # noqa
    template_name = 'index.html'
    context = {}

    def get(self, request):
        products = Product.objects.all()[:4]
        product_data = []
        for product in products:
            image = Picture.objects.filter(product=product).first()
            product.image = image
            product_data.append(product)

        self.context.update({'products': product_data})
        return render(request, self.template_name, self.context)

    def post(self, request): # noqa
        id = request.POST.get('id') # noqa
        user = request.user
        shopping_cart = ShoppingCard.objects.filter(Q(product_id=id) & Q(user=user))
        if not shopping_cart:
            shopping_cart = ShoppingCard.objects.create(
                product_id=id,
                user=user
            )
            shopping_cart.save()
            messages.info(request, "Added successfully!")
            return redirect('/')
        return redirect('/cart')


def about(request):
    return render(request, "about.html")


def shop(request):
    return render(request, "shop.html")


class ShoppingCardView(View):  # noqa
    template_name = 'cart.html'
    context = {}

    def get(self, request):
        shopping_cart = ShoppingCard.objects.filter(user=request.user)
        products = Product.objects.filter(pk__in=shopping_cart)
        data = []
        for product in products:
            shop = ShoppingCard.objects.get(Q(user=request.user) & Q(product=product))  # noqa
            product.count = shop.count
            data.append(product)
        self.context.update({'products': data})
        return render(request, self.template_name, self.context)

    def post(self, request):  # noqa
        id = request.POST.get('id')  # noqa
        user = request.user
        shopping_cart = ShoppingCard.objects.get(Q(product_id=id) & Q(user=user))
        shopping_cart.delete()
        return redirect('/cart')


class IncrementCountView(View):

    def post(self, request):  # noqa
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            id = json_data.get('id') # noqa
        except json.JSONDecodeError:
            id = None  # noqa
        result = increment_count(id, request.user)
        return JsonResponse({'result': result})


class DecrementCountView(View):

    def post(self, request):  # noqa
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            id = json_data.get('id')  # noqa
        except json.JSONDecodeError:
            id = None  # noqa
        result = decrement_count(id, request.user)
        return JsonResponse({'result': result})


def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")


def shop_single(request):
    return render(request, "shop-single.html")


def thankyou(request):
    return render(request, "thankyou.html")


class AddProductView(View):
    form_class = ProductForm
    template_name = 'add_product.html'

    def get(self, request):
        form = self.form_class() # noqa
        return render(request, self.template_name)

    def post(self, request): # noqa


        name = request.POST.get('product_name') # noqa
        price = request.POST.get('product_price')
        description = request.POST.get('product_description')
        author = request.user


        product = Product.objects.create( # noqa
            name=name,
            price=price,
            description=description,
            user=author,
        )

        images = request.FILES.getlist('product_image')

        for image in images:
            picture = Picture.objects.create(
                image=image,
                product=product
            )
            picture.save()
        return redirect('/')


class DeleteProductView(DeleteView):  # noqa
    model = Product
    template_name = ''
    success_url = '/'  # noqa
