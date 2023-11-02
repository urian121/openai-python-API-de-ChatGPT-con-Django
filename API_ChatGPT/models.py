from django.db import models

# Create your models here.


class HistorialChatPregunta(models.Model):
    id_historial = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=False, null=False)
    pregunta = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = "tbl_chat_preguntas"
        ordering = ['-created_at']


class HistorialChatRespuestas(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    historial_id = models.ForeignKey(
        HistorialChatPregunta, on_delete=models.CASCADE)
    respuesta = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = "chat_respuestas"
        ordering = ['-created_at']
