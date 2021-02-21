from django.db import models
from django.urls import reverse

class Product(models.Model):
    color_list = ['none', 'alb', 'negru', 'roz', 'albastru',
                  'galben', 'gri', 'rosu', 'verde', 'mov', 'portocaliu']
    colors_choises = []
    for i in color_list:
        colors_choises.append((i.upper(), i))
    image = models.ImageField()

    name = models.CharField(max_length=25, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=250, null=True, blank=True)
    color =models.CharField(max_length=10, choices=colors_choises, default=colors_choises[0])

    def get_absolute_url(self):
        return reverse('products:product_detail',kwargs={'id':self.id})
        # After a product is created, switch to it's page

    def __str__(self):
        return self.name
