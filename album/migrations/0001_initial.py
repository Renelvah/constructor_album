# Generated by Django 3.1.5 on 2021-04-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cover', models.CharField(max_length=40)),
                ('color', models.CharField(choices=[('black', 'Черный'), ('blue', 'Синий'), ('red', 'Красный'), ('white', 'Белый')], default='black', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=15)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='album.album')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(db_index=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper', models.CharField(db_index=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(default='20x20', max_length=10)),
                ('pages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(db_index=True, default='Праздник', max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('text', models.TextField(blank=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='album.package'),
        ),
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='album.size'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.buyer'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('text', models.TextField(blank=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.album')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='album.buyer')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='album.cover'),
        ),
        migrations.AddField(
            model_name='album',
            name='paper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='album.paper'),
        ),
        migrations.AddField(
            model_name='album',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='album.size'),
        ),
    ]
