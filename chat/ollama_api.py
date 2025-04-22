import csv
import ollama
import random
from faker import Faker

fake = Faker()
model_name = 'granite3.2:latest'

age = random.randrange(21,60)
level = random.choice(["minor","major","critical"])
intensity = random.choice(["low","medium","high"])
name = fake.name()
job = fake.job()
spirits = random.choice(["low","medium","high"])
csv_file = "patient_profiles.csv"

def read_csv(csv_file):
    with open(csv_file, "r") as f:
        data = csv.DictReader(f)
        data_list = []
        for row in data:
            data_list.append(row)
    return data_list

data_list = read_csv(csv_file)
individuals = random.choices(data_list,k=4)

def generate_response(user_input):
        messages = [
{"role": "user", "content": f"""
You are a patient designed for a doctor to practice Motivation Interviewing based off of the following individuals:

{individuals}

"""
},
{"role": "system", "content": f"""
You're name is {name} and are {age} and a professional {job} but has some type
 of {level} health issue, that is inspired from these previous individuals. You
 want to be {intensity} level of attitude to get help and you seem in {spirits}
 level of happiness. Only describe the name and general information about the
 individual you create, you're job is to work with the person asking the
 questions to have them figure out how to have them make healthy choices.
"""
},
]
        response = ollama.chat(model=model_name, messages=messages)
        messages.append({"role": "user", "content": user_input})
        response = ollama.chat(model=model_name, messages=messages)
        answer = response.message.content
        messages.append({"role": "assistant", "content": answer})
        output_dict = {"content": answer,
                       "name": name,
                       "age": age,
                       "job": job,
                       "spirits": spirits,
                       "help": intensity
                      }
        return output_dict
