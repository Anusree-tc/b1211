from django.db import models
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(blank=True)
    image=models.FileField(upload_to='category',null=True)
    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])


class Product(models.Model):

    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(blank=True)
    image=models.FileField(upload_to='category',null=True)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


    def get_url(self):

        return reverse('product_det', args=[self.category.slug,self.slug])




    def __str__(self):
         return '{}'.format(self.name)
