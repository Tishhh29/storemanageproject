# Generated by Django 4.2.4 on 2023-09-01 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.store'),
        ),
    ]
