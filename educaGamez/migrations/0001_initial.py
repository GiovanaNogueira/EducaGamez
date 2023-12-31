# Generated by Django 3.2.13 on 2023-06-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcaoA', models.BooleanField()),
                ('opcaoB', models.BooleanField()),
                ('opcaoC', models.BooleanField()),
                ('opcaoD', models.BooleanField()),
            ],
        ),
    ]
