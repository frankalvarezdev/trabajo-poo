# Generated by Django 3.1.2 on 2020-10-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='date',
            field=models.IntegerField(default=0),
        ),
    ]