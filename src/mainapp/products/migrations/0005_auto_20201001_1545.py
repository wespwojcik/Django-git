# Generated by Django 2.1.5 on 2020-10-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201001_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('drinks', 'drinks'), ('treats', 'treats')], max_length=60),
        ),
    ]
