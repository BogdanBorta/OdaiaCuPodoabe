from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=250, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name
