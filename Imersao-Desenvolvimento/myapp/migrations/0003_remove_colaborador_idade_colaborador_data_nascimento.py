# Generated by Django 5.1 on 2024-09-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_emprestimo_quantidade_equipamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='idade',
        ),
        migrations.AddField(
            model_name='colaborador',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
    ]
