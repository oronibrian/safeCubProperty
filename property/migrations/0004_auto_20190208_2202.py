# Generated by Django 2.1.5 on 2019-02-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_propertyfile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertyfile',
            options={'verbose_name': 'Property file', 'verbose_name_plural': 'Property files'},
        ),
        migrations.AlterField(
            model_name='propertyfile',
            name='file',
            field=models.FileField(upload_to='property/docs', verbose_name='file'),
        ),
    ]