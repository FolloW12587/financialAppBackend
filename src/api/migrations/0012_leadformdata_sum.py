# Generated by Django 3.2.9 on 2022-02-11 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_leadformdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadformdata',
            name='sum',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Сумма'),
        ),
    ]
