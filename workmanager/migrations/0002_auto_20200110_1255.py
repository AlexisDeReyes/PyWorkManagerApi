# Generated by Django 3.0.2 on 2020-01-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
