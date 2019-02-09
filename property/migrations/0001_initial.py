# Generated by Django 2.1.5 on 2019-02-08 18:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('address', models.TextField(verbose_name='address')),
                ('notes', models.TextField(blank=True, verbose_name='notes')),
                ('area', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='surface area')),
                ('rooms', models.DecimalField(decimal_places=0, max_digits=2, validators=[django.core.validators.MinValueValidator(1)], verbose_name='number of rooms')),
            ],
            options={
                'verbose_name': 'property',
                'verbose_name_plural': 'properties',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='property_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Property Location',
                'verbose_name_plural': 'Property Locations',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('notes', models.TextField(blank=True, verbose_name='notes')),
            ],
            options={
                'verbose_name': 'Property Type',
                'verbose_name_plural': 'Property Types',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='property.property_location', verbose_name='Property Location'),
        ),
    ]
