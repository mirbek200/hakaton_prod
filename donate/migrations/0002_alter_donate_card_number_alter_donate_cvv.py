# Generated by Django 4.1.1 on 2022-10-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='card_number',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='donate',
            name='cvv',
            field=models.CharField(max_length=3),
        ),
    ]
