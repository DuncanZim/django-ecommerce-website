# Generated by Django 2.2 on 2019-07-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20190718_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='amount',
            field=models.FloatField(default=50),
            preserve_default=False,
        ),
    ]