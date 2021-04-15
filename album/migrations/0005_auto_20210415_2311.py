# Generated by Django 3.1.5 on 2021-04-15 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_remove_cover_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='album.theme'),
        ),
    ]