# Generated by Django 3.1.5 on 2021-04-15 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0006_auto_20210415_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='package',
            field=models.ForeignKey(default=5, null=True, on_delete=django.db.models.deletion.PROTECT, to='album.package'),
        ),
    ]
