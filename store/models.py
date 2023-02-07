from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    price = models.IntegerField()
    description = models.TextField(max_length=500,blank=True)
    image =models.ImageField(upload_to='photos/product')
    stock = models.IntegerField()
    is_avilable = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    modified_time = models.DateField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug,self.slug])
    def __str__(self):
        return self.product_name
