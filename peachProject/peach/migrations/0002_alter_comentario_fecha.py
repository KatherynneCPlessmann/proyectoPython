# Generated by Django 3.2.5 on 2022-06-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peach', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateField(),
        ),
    ]