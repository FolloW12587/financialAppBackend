# Generated by Django 3.2.9 on 2022-04-12 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20220216_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Приложение',
                'verbose_name_plural': 'Приложения',
            },
        ),
        migrations.AddField(
            model_name='settings',
            name='app',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.app', verbose_name='Приложение'),
        ),
    ]
