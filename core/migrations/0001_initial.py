# Generated by Django 3.1.7 on 2021-04-20 13:37

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
                ('your_name', models.CharField(max_length=50)),
                ('your_email', models.EmailField(max_length=254)),
                ('your_subject', models.CharField(max_length=100)),
                ('your_message', models.TextField()),
            ],
        ),
    ]
