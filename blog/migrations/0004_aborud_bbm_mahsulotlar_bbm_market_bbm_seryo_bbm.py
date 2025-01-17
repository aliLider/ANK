# Generated by Django 4.2.6 on 2025-01-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='aborud',
            name='bbm',
            field=models.BooleanField(default=False, verbose_name="BBMga qo'shilganmi"),
        ),
        migrations.AddField(
            model_name='mahsulotlar',
            name='bbm',
            field=models.BooleanField(default=False, verbose_name="BBMga qo'shilganmi"),
        ),
        migrations.AddField(
            model_name='market',
            name='bbm',
            field=models.BooleanField(default=False, verbose_name='bbm'),
        ),
        migrations.AddField(
            model_name='seryo',
            name='bbm',
            field=models.BooleanField(default=False),
        ),
    ]
