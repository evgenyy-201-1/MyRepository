# Generated by Django 4.0.3 on 2022-03-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_options_remove_product_cast_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='notice',
            field=models.TextField(blank=True, verbose_name='Примечание к товару'),
        ),
    ]
