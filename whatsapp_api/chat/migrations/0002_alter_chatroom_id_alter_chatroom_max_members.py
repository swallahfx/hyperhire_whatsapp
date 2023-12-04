# Generated by Django 4.2.7 on 2023-11-30 11:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='max_members',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]