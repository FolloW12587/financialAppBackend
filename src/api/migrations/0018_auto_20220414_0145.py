# Generated by Django 3.2.9 on 2022-04-14 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20220414_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialunit',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='financialunit',
            name='loan_terms',
            field=models.TextField(blank=True, default='', verbose_name='Условия займа'),
        ),
        migrations.AlterField(
            model_name='financialunit',
            name='requirements',
            field=models.TextField(blank=True, default='', verbose_name='Требования'),
        ),
    ]