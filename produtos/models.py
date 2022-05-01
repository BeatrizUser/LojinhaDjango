from django.db import models
from uuid import uuid4

def upload_image_produto(instance, filename):
    return f"{instance.id_produto}-{filename}"


class Produtos(models.Model):
    SHIRTS_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )
    SHIRTS_COLORS = (
        ('B', 'Blue'),
        ('Bk', 'Black'),
        ('W', 'White'),
        ('R', 'Red'),
    )

    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    size = models.CharField(max_length=3, choices=SHIRTS_SIZES)
    color = models.CharField(max_length=3, choices=SHIRTS_COLORS)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to=upload_image_produto, blank=True, null=True)