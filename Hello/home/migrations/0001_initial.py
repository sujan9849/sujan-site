# Generated by Django 3.0.6 on 2020-05-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
