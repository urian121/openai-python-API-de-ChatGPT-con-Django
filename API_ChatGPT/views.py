from django.shortcuts import render, redirect
import logging
from django.db.utils import DataError, DatabaseError
from django.http import JsonResponse, HttpResponse
from . models import *


def inicio(request):
    return render(request, 'index.html')


def solicitud_chat_gpt(request):
    if request.method == 'POST':
        try:
            ask = request.POST.get('pregunta')
            user = request.POST.get('usuario')

            chat = ChatPregunta(usuario=user, pregunta=ask)
            chat.save()

            # Obtén el último id_pregunta generado para el registro insertado
            ultimo_id = chat.id_pregunta

            return JsonResponse({'status': 200, 'ultimo_id': ultimo_id})
        except (DataError, DatabaseError) as e:
            logging.error("Error en la vista solicitud_chat_gpt: %s", str(e))
    return redirect('inicio')
