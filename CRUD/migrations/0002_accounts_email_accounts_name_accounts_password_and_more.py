# Generated by Django 4.0.1 on 2022-01-20 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='Email',
            field=models.EmailField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Password',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Phone',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Username',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]