import csv
import ollama
import os
import random
import logging
from ollama import Client


model_name = 'granite3.2:latest'
ollama_host = os.environ.get('OLLAMA_SELF_HOST', '127.0.0.1')


def create_json_content(patient, file_content=None):
        system_content = f"""
 You will answer the question if the student asks one about the MITI
 interviewing style. If the don't ask a direct question, read the conversation
 that is attached to the prompt and give advice on how they can improve their
 interviews. Also if they give you a complete conversation, give an output of
 the rubric for the MITI process.

IMPORTANT: Format your responses using markdown for better readability:
- Use **bold** for emphasis on important points and key concepts
- Use *italic* for examples or specific techniques
- Use bullet points for lists of suggestions or improvements
- Use numbered lists for step-by-step instructions
- Use > for important quotes or key principles
- Use `code` formatting for specific MITI terms or scores
- Use headers (##) for organizing different sections (e.g., "## Areas for Improvement", "## Recommendations")
- Structure your responses with clear paragraphs
- Use tables for rubric scores when applicable
"""
        # If file content is provided, append it to the system message
        if file_content:
            system_content += f"\n\nAdditional context from uploaded file:\n{file_content}"

        messages = [
{"role": "user", "content": f"""
You are a teacher of the Motivation Interviewing Treatement Integrity process
 for Doctors and medical students. Your goal is to get the user to recieve the
 highest score possible on the MITI rubic and come back with advice on better
 ways to engage with the patients.

"""
},
{"role": "system", "content": system_content},
]
        return messages

def create_messages(patient, file_content=None):
    messages = create_json_content(patient, file_content)
    return messages

def generate_response(user_input, messages, patient, file_content=None):
    # Ensure the previous_chats directory exists
    os.makedirs("previous_chats", exist_ok=True)
    
    logging.basicConfig(
        level=logging.CRITICAL,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=f"previous_chats/suggestions.log",
    )
    client = Client(
          host=f'http://{ollama_host}:11434',
    )
    if messages is None:
        messages = create_messages(patient, file_content)
    response = client.chat(model=model_name, messages=messages)
    messages.append({"role": "user", "content": user_input})
    logging.critical(f"Me: {user_input}")
    response = client.chat(model=model_name, messages=messages)
    answer = response.message.content
    messages.append({"role": "assistant", "content": answer})
    output_dict = {"content": answer,
                  }
    logging.critical(f"PETE Tutor: {answer}")
    return output_dict
