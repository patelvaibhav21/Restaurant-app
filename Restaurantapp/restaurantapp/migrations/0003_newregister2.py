# Generated by Django 4.1.1 on 2022-10-06 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0002_newregister1'),
    ]

    operations = [
        migrations.CreateModel(
            name='newregister2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=130)),
                ('lastname', models.CharField(max_length=130)),
                ('email', models.CharField(max_length=130)),
                ('password', models.CharField(max_length=130)),
                ('date', models.DateField()),
            ],
        ),
    ]
