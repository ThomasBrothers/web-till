from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount_sold = models.IntegerField(default = 0)
    time_stamp = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.product
