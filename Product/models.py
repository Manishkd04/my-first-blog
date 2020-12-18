from django.db import models
from Category.models import Category, Sub_category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='upload/products/')

    def __str__(self):
        return self.name

    def snipet(self):
        return self.name[: 100] + '...'

    
