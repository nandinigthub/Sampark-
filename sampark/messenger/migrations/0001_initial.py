# Generated by Django 4.1.3 on 2023-07-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='messenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_number', models.CharField(default='+91', max_length=20)),
                ('msg', models.CharField(default='none', max_length=200)),
            ],
        ),
    ]
