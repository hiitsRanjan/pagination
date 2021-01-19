from django.db import models

class ProductModels(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="product_images/")
    category = models.CharField(max_length=100,default="Mobile")