from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()

# class Product(models.Model): # noqa
#     name = models.CharField(max_length=150)
#     price = models.FloatField()
#     image = models.ImageField(upload_to='pics')
#     description = models.TextField()
#
#     # def save(self, validated_data, obj: Union["Product", "Picture"]): # noqa
#     #
#     #     return super().save(**validated_data)
class Product(models.Model): # noqa
    name = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def create(self, validated_data):
        print(validated_data)
        return super().save(**validated_data)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


# class Picture(models.Model):
#     image = models.ImageField(upload_to='pics')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
class Picture(models.Model):
    image = models.ImageField(upload_to='pics')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Picture')
        verbose_name_plural = _('Pictures')


# class ShoppingCard(models.Model): # noqa
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     count = models.IntegerField(default=1)
#     uploaded_date = models.DateTimeField(auto_now_add=True)


class ShoppingCard(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    uploaded_date = models.DateTimeField(auto_now_add=True)

# user: admin password:secdet123 # noqa
# user: jamshid password:1a2s3d4f # noqa
