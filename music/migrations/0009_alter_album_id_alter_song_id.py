# Generated by Django 4.2.8 on 2023-12-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_album_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
