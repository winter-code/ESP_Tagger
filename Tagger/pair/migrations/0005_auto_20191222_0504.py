# Generated by Django 3.0.1 on 2019-12-22 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pair', '0004_auto_20191222_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pair.User'),
        ),
    ]