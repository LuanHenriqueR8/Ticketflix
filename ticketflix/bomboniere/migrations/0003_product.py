# Generated by Django 2.0.8 on 2018-11-20 02:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bomboniere', '0002_combo_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome', max_length=50, verbose_name='Nome')),
                ('description', models.TextField(blank=True, help_text='Descrição', max_length=200, null=True, verbose_name='Descrição')),
                ('price', models.FloatField(help_text='Preço', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço')),
                ('quantity', models.IntegerField(blank=True, help_text='Quantidade de Produtos no Combo', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]