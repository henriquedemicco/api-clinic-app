# Generated by Django 3.0.7 on 2021-12-21 16:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('sexo', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=100)),
                ('celular', models.ImageField(blank=True, max_length=300, null=True, upload_to='media')),
                ('data_nascimento', models.DateField()),
                ('email', models.CharField(max_length=10)),
            ],
        ),
    ]
