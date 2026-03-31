from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    Product_Type = (
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Books', 'Books'),
    )
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date = models.DateField(default=timezone.now)
    product_type = models.CharField(max_length=100, choices=Product_Type)
    
    def __str__(self):
        return self.name


