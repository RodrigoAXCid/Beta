# Generated by Django 4.1.1 on 2022-09-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=30)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
