# Generated by Django 4.0.4 on 2022-05-01 00:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0011_remove_produtos_id_shirt_produtos_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='id',
        ),
        migrations.AddField(
            model_name='produtos',
            name='id_produto',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
