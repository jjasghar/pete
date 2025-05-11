from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from .ollama_api import generate_response, create_messages
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedFile
import json
import markdown

# Create your views here.

patient = None
messages = None
current_file_content = None

@csrf_exempt
def suggestions_view(request):

    global messages, current_file_content

    if request.method == "POST":
        prompt = request.POST.get("message", "")
        
        # Handle file upload
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            
            # Validate file type
            if uploaded_file.name.endswith(('.log', '.txt')):
                # Save the file
                file_obj = UploadedFile.objects.create(
                    file=uploaded_file,
                    filename=uploaded_file.name
                )
                
                # Read file content
                current_file_content = file_obj.get_file_content()
                
                # Reset messages to include new file content
                messages = None
                
                return JsonResponse({
                    "content": f"File '{uploaded_file.name}' uploaded successfully. File content has been loaded and will be used as context for future responses."
                })
            else:
                return JsonResponse({
                    "content": "Error: Only .log and .txt files are allowed."
                })
        
        # Handle regular message
        if prompt:
            response = generate_response(prompt, messages, patient, current_file_content)
            # Convert markdown to HTML
            response['content'] = markdown.markdown(response['content'], extensions=['fenced_code', 'codehilite', 'tables', 'nl2br'])
            return JsonResponse(response)
            
    return render(request, "suggestions.html")

def reload_chat(request):

    global messages, current_file_content

    messages = None
    current_file_content = None
    return suggestions_view(request)
