# Generated by Django 3.2.3 on 2021-05-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_novo_app', '0006_auto_20210521_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sub_grupos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
