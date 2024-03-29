# Generated by Django 3.2.9 on 2022-02-11 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_settings_settings_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadFormData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('email', models.CharField(max_length=255, verbose_name='Почта')),
                ('phone', models.CharField(max_length=31, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Данные с лид формы',
                'verbose_name_plural': 'Данные с лид формы',
            },
        ),
    ]
