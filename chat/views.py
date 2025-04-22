from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from .ollama_api import generate_response
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        user_input = request.POST["message"]
        prompt = f"User: {user_input}\nAI:"
        response = generate_response(prompt)
        out = JsonResponse(response)
        return out
    return render(request, "chat.html")
