from dasa import calculate_dasa
from datetime import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

def cutString(text):
    start_index = text.find('{')
    end_index = text.rfind('}')

    json_substring = text[start_index:end_index + 1]
    return json_substring

client = OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)

def panchangPrompt(panchang,index,name,gender):
    if index == 0:
        prompt = f"{name}, who was born on {panchang['paksha']} Paksha {panchang['thithi']}. use {name} and {gender} pronouns all over the content. Explain {name}'s birth Thithi characteristics, including personality traits and emotional/mental state, in a short abstract single paragraph."
        
    if index == 1:
        prompt = f"{name}, who was born on {panchang['week_day']}.use {name} and {gender} pronouns all over the content. Describe {name}'s birth Vaaram characteristics, such as unique traits and their impact on the child's life, in a short single paragraph."
        
    if index == 2:
        prompt = f"{name}, who was born under the {panchang['nakshatra']} Nakshatra.use {name} and {gender} pronouns all over the content. Provide insights into {name}'s Nakshatra characteristics, including personality traits and life path, in a short single paragraph."

    if index == 3:
        prompt = f"{name}, who was born under the {panchang['yoga']} Yogam.use {name} and {gender} pronouns all over the content. Provide insights into {name}'s Yogam characteristics, including goals, spiritual growth, and overall impact, in a short single paragraph."
        
    if index == 4:
        prompt = f"{name}, who was born under the {panchang['karanam']} Karanam.use {name} and {gender} pronouns all over the content. Provide insights into {name}'s Karanam characteristics, including approaches to tasks, work habits, success strategies, and achievements, in a short single paragraph."
      
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=4096,
        messages=[
            {
                "role": "user", "content": prompt
            }
        ]
    )
      
    res = completion.choices[0].message.content
    print(res)
    return res