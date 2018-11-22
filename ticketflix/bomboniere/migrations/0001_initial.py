# Generated by Django 2.0.8 on 2018-11-20 02:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome', max_length=50, verbose_name='Nome')),
                ('description', models.TextField(blank=True, help_text='Descrição', max_length=200, null=True, verbose_name='Descrição')),
                ('price', models.FloatField(help_text='Preço', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço')),
            ],
            options={
                'verbose_name': 'Combo',
                'verbose_name_plural': 'Combos',
            },
        ),
    ]
