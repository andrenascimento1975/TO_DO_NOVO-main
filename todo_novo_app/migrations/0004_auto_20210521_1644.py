# Generated by Django 3.1.7 on 2021-05-21 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_novo_app', '0003_auto_20210521_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_grupos',
            name='grupo_sub',
        ),
        migrations.AddField(
            model_name='grupos',
            name='sub_grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupo_sub', to='todo_novo_app.sub_grupos'),
        ),
    ]