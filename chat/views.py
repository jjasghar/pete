from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from .ollama_api import generate_response, create_messages, create_patient, setup_logging
from django.views.decorators.csrf import csrf_exempt
import json
import markdown

# Create your views here.

patient = None
messages = None

@csrf_exempt
def chat_view(request):

    global patient
    global messages

    if patient is None:
        patient = create_patient()
        messages = create_messages(patient)
        # Setup logging for the new patient
        setup_logging(patient)

    context = {"name": patient.name, "age": patient.age, "job": patient.job}
    if request.method == "POST":
       prompt = request.POST["message"]
       response = generate_response(prompt, messages, patient)
       # Convert markdown to HTML
       response['content'] = markdown.markdown(response['content'], extensions=['fenced_code', 'codehilite', 'tables', 'nl2br'])
       out = JsonResponse(response)
       return out
    return render(request, "chat.html", context)

def reload_chat(request):

    global patient
    global messages

    messages = None
    patient = None
    response = chat_view(request)
    return response
