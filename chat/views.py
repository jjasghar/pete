from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from .ollama_api import generate_response, create_messages, create_patient
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

patient = create_patient()
messages = create_messages(patient)

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        user_input = request.POST["message"]
        prompt = f"User: {user_input}\nAI:"
        response = generate_response(prompt, messages, patient)
        out = JsonResponse(response)
        return out
    return render(request, "chat.html")

def reload_chat(request):
    messages = None
    patient = None
    patient = create_patient()
    messages = create_messages(patient)
    response = chat_view(request)
    return response
