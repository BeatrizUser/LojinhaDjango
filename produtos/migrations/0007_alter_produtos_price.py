# Generated by Django 4.0.4 on 2022-04-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_alter_produtos_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
