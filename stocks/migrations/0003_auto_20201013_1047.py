# Generated by Django 3.1.1 on 2020-10-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20201012_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='last_value',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
