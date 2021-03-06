# Generated by Django 3.0.2 on 2020-01-12 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200107_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartline',
            name='cart_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Cart'),
        ),
        migrations.AlterField(
            model_name='cartline',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='If you want to register as company please click on checkbox :) ', verbose_name='for companies :'),
        ),
        migrations.AlterField(
            model_name='wishlistline',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
        migrations.AlterField(
            model_name='wishlistline',
            name='wishlist_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Wishlist'),
        ),
    ]
