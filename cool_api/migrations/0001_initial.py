# Generated by Django 3.2.6 on 2021-08-20 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FtpLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True, verbose_name='Date')),
                ('username', models.CharField(max_length=120, null=True, verbose_name='Username')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('status', models.CharField(max_length=10, null=True, verbose_name='Status')),
            ],
        ),
    ]
