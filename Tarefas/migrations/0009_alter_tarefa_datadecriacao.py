# Generated by Django 5.0.1 on 2024-01-05 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarefas', '0008_alter_tarefa_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='DataDeCriacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='teste'),
        ),
    ]
