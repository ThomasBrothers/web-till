# Generated by Django 2.1.3 on 2018-12-03 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('till', '0004_auto_20181203_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='products_from_trans',
        ),
        migrations.AddField(
            model_name='sale',
            name='products_sold',
            field=models.ManyToManyField(blank=True, null=True, related_name='le_sales', to='till.SaleTracker'),
        ),
    ]