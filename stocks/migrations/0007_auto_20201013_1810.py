# Generated by Django 3.1.1 on 2020-10-13 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0006_auto_20201013_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='users',
        ),
        migrations.AddField(
            model_name='stock',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stocks', to=settings.AUTH_USER_MODEL),
        ),
    ]
