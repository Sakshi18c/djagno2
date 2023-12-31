# Generated by Django 4.2.2 on 2023-07-03 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sakhi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='mobile',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
