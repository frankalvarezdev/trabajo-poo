# Generated by Django 3.1.2 on 2020-10-14 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0006_productos_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='provider',
            field=models.IntegerField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
