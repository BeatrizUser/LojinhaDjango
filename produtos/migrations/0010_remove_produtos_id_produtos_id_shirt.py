# Generated by Django 4.0.4 on 2022-04-30 21:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_produtos_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='id',
        ),
        migrations.AddField(
            model_name='produtos',
            name='id_shirt',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
