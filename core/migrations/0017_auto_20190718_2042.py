# Generated by Django 2.2 on 2019-07-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
