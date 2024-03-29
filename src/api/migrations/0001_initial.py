# Generated by Django 3.2.9 on 2021-11-16 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancailUnitsType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=127, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Тип финансовой единицы',
                'verbose_name_plural': 'Типы финансовых единиц',
            },
        ),
        migrations.CreateModel(
            name='FinancialUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('short_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Короткое описание')),
                ('range_str', models.CharField(blank=True, max_length=255, null=True, verbose_name='Диапазон')),
                ('active', models.BooleanField(default=True, verbose_name='Активно')),
                ('fin_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.financailunitstype', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Финансовая единица',
                'verbose_name_plural': 'Финансовые единицы',
            },
        ),
    ]
