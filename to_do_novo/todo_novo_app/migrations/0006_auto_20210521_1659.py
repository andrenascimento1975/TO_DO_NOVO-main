# Generated by Django 3.1.7 on 2021-05-21 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_novo_app', '0005_auto_20210521_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_grupos',
            name='grupo_sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='join_grupos', to='todo_novo_app.grupos'),
        ),
    ]