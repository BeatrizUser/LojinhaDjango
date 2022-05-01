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
        ('blue', 'Blue'),
        ('black', 'Black'),
        ('white', 'White'),
        ('red', 'Red'),
    )
    
    id_produto = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=250)
    size = models.CharField(max_length=10, choices=SHIRTS_SIZES)
    color = models.CharField(max_length=10, choices=SHIRTS_COLORS)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=upload_image_produto, blank=True, null=True)

    class Meta:
        ordering = ("title",)