# Generated by Django 3.2.2 on 2021-05-22 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20210522_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='child_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.folder'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]
