# Generated by Django 4.2.6 on 2025-01-07 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_orderitem_order_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahsulot_nomi', models.TextField(verbose_name="Mahsulotlar ro'yxati")),
                ('umumiy_summa', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Umumiy summa')),
                ('buyurtma_vaqti', models.DateTimeField(auto_now_add=True, verbose_name='Buyurtma vaqti')),
                ('foydalanuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
        ),
    ]
