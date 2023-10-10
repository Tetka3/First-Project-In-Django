# Generated by Django 4.2.5 on 2023-10-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('nights', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
