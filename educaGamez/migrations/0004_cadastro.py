# Generated by Django 3.2.13 on 2023-06-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educaGamez', '0003_auto_20230616_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('usuario', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('escola', models.CharField(max_length=100)),
                ('serie', models.CharField(max_length=15)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
    ]
