# Generated by Django 4.2.6 on 2025-01-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_aborud_group_lang_alter_mahsulotlar_group_lang_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahsulotlar',
            name='rangi',
        ),
        migrations.AlterField(
            model_name='aborud',
            name='group_lang',
            field=models.CharField(choices=[('en', 'en'), ('ru', 'ru'), ('uz', 'uz')], default='uz', max_length=100),
        ),
        migrations.AlterField(
            model_name='mahsulotlar',
            name='group_lang',
            field=models.CharField(choices=[('en', 'en'), ('ru', 'ru'), ('uz', 'uz')], default='uz', max_length=100),
        ),
        migrations.AlterField(
            model_name='market',
            name='group_lang',
            field=models.CharField(choices=[('en', 'en'), ('ru', 'ru'), ('uz', 'uz')], default='uz', max_length=100),
        ),
        migrations.AlterField(
            model_name='seryo',
            name='group_lang',
            field=models.CharField(choices=[('en', 'en'), ('ru', 'ru'), ('uz', 'uz')], default='uz', max_length=100),
        ),
    ]
