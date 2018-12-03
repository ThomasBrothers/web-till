from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def get_all_sales(self):
        if(self.completed_sales.count() > 0):
            return self.completed_sales.count()
        else:
            return 0


class Sale(models.Model):
    products_sold = models.ManyToManyField('SaleTracker', related_name='le_sales', null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Sale: {0}, Primary Key: {1}".format(self.time_stamp, self.pk)


class SaleTracker(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='trackers')
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='receipts')
    amount_sold = models.IntegerField(default=0)

    def __str__(self):
        return "{0}".format(self.product)


