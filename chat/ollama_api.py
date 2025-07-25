import csv
import ollama
import os
import random
import logging
from faker import Faker
from ollama import Client

class Patient:
    def __init__(self, age, level, intensity, name, job, spirits):
        self.age = age
        self.level = level
        self.intensity = intensity
        self.name = name
        self.job = job
        self.spirits = spirits

fake = Faker()
model_name = 'granite3.2:latest'
# Default to adult profiles, will be updated based on selection
csv_file = "profiles/adult_patient_profiles.csv"
ollama_host = os.environ.get('OLLAMA_SELF_HOST', '127.0.0.1')

def read_csv(csv_file):
    with open(csv_file, "r") as f:
        data = csv.DictReader(f)
        data_list = []
        for row in data:
            data_list.append(row)
    return data_list

# Global variables to store profile data
adult_data_list = None
pediatric_data_list = None
current_individuals = None

def get_profile_data(profile_type="adult"):
    """Get profile data based on the selected profile type"""
    global adult_data_list, pediatric_data_list
    
    if profile_type == "pediatric":
        if pediatric_data_list is None:
            pediatric_data_list = read_csv("profiles/child_patient_profiles.csv")
        return pediatric_data_list
    else:  # adult
        if adult_data_list is None:
            adult_data_list = read_csv("profiles/adult_patient_profiles.csv")
        return adult_data_list

def create_json_content(patient, profile_type="adult"):
        global current_individuals
        
        # Get the appropriate profile data
        data_list = get_profile_data(profile_type)
        current_individuals = random.choices(data_list, k=4)
        
        messages = [
{"role": "user", "content": f"""
You are a patient designed for a doctor to practice Motivation Interviewing based off of the following individuals:

{current_individuals}

"""
},
{"role": "system", "content": f"""
You're name is {patient.name} and are {patient.age} and a professional
 {patient.job} but has some type of {patient.level} health issue, that is inspired from these previous individuals. You
 want to be {patient.intensity} level of attitude to get help and you seem in
 {patient.spirits} level of happiness. Only describe the name and general information about the
 individual you create, you're job is to work with the person asking the
 questions to have them figure out how to have them make healthy choices.
 You {random.choice(["never","sometimes","always"])} want to be addressed with
 your name or nickname, not something completely different.

IMPORTANT: Format your responses using markdown for better readability:
- Use **bold** for emphasis on important points
- Use *italic* for personal feelings or thoughts
- Use bullet points for lists
- Use > for quotes or important statements
- Use `code` formatting for specific terms or measurements
- Structure your responses with clear paragraphs
- Use headers (##) for organizing different topics if needed
"""
},
]
        return messages

def create_patient(profile_type="adult"):
    if profile_type == "pediatric":
        # Pediatric patients: ages 2-18, different job descriptions
        age = random.randrange(2, 19)
        level = random.choice(["minor","major","critical"])
        intensity = random.choice(["low","medium","high"])
        name = fake.name()
        
        # More appropriate job descriptions for children
        if age < 5:
            job = "preschooler"
        elif age < 12:
            job = "elementary student"
        elif age < 18:
            job = "student"
        else:
            job = "student"
            
        spirits = random.choice(["low","medium","high"])
    else:
        # Adult patients: ages 21-60, with jobs
        age = random.randrange(21, 60)
        level = random.choice(["minor","major","critical"])
        intensity = random.choice(["low","medium","high"])
        name = fake.name()
        job = fake.job()
        spirits = random.choice(["low","medium","high"])

    patient = Patient(age, level, intensity, name, job, spirits)
    return patient

def create_messages(patient, profile_type="adult"):
    messages = create_json_content(patient, profile_type)
    return messages

def setup_logging(patient):
    """Setup logging configuration for a new patient"""
    # Ensure the previous_chats directory exists
    os.makedirs("previous_chats", exist_ok=True)
    
    # Sanitize filename to avoid path issues
    safe_name = patient.name.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
    safe_job = patient.job.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
    
    # Clear any existing handlers to avoid duplicate logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    logging.basicConfig(
        level=logging.CRITICAL,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=f"previous_chats/{safe_name}-{patient.age}-{safe_job}.log",
        force=True
    )

def generate_response(user_input, messages, patient):
    client = Client(
          host=f'http://{ollama_host}:11434',
    )
    response = client.chat(model=model_name, messages=messages)
    messages.append({"role": "user", "content": user_input})
    logging.critical(f"Me: {user_input}")
    response = client.chat(model=model_name, messages=messages)
    answer = response.message.content
    messages.append({"role": "assistant", "content": answer})
    output_dict = {"content": answer,
                   "name": patient.name,
                   "age": patient.age,
                   "job": patient.job,
                   "spirits": patient.spirits,
                   "help": patient.intensity
                  }
    logging.critical(f"{patient.name}: {answer}")
    return output_dict
