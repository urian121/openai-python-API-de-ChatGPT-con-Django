# Generated by Django 4.2.7 on 2023-11-03 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API_ChatGPT', '0002_alter_historialchatrespuestas_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistorialChatPregunta',
            new_name='ChatPregunta',
        ),
        migrations.RenameModel(
            old_name='HistorialChatRespuestas',
            new_name='ChatRespuestas',
        ),
        migrations.RenameField(
            model_name='chatpregunta',
            old_name='id_historial',
            new_name='id_pregunta',
        ),
    ]