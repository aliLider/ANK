# Generated by Django 5.1.4 on 2025-01-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_aborud_group_lang_alter_mahsulotlar_group_lang_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aborud',
            name='group_lang',
            field=models.CharField(choices=[('en', 'en'), ('uz', 'uz'), ('ru', 'ru')], default='uz', max_length=100),
        ),
        migrations.AlterField(
            model_name='mahsulotlar',
            name='group_lang',
            field=models.CharField(choices=[('en', 'en'), ('uz', 'uz'), ('ru', 'ru')], default='uz', max_length=100),
        ),
        migrations.AlterField(
            model_name='market',
            name='group_lang',
            field=models.CharField(choices=[('en', 'en'), ('uz', 'uz'), ('ru', 'ru')], default='uz', max_length=100),
        ),
        migrations.AlterField(
            model_name='seryo',
            name='group_lang',
            field=models.CharField(choices=[('en', 'en'), ('uz', 'uz'), ('ru', 'ru')], default='uz', max_length=100),
        ),
    ]
