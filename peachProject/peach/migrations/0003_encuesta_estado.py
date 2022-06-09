# Generated by Django 3.2.5 on 2022-06-04 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peach', '0002_alter_comentario_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(max_length=80)),
                ('experiencia', models.IntegerField(max_length=2)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peach.estado')),
            ],
        ),
    ]