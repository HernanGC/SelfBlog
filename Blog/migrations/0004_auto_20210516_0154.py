# Generated by Django 3.2.2 on 2021-05-16 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_navbaritem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbaritem',
            name='onclick',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='navbaritem',
            name='view',
            field=models.CharField(default='', max_length=25),
        ),
    ]