from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)

number_words = {
    2: "Second",
    3: "Third",
    4: "Fourth",
    5: "Fifth",
    6: "Sixth",
    7: "Seventh",
    8: "Eighth",
    9: "Ninth",
    10: "Tenth",
    11: "Eleventh",
    12: "Twelfth"
}

def PlanetPrompt(planets,name,gender):
    content = f"""Create a Planet Position detailed report for a {name} whose {planets['Name']} Placed in {planets['pos_from_asc']} House of {planets['sign']} Sign in {planets['nakshatra']} Nakshatra use {name} and {gender} pronouns all over the content"""
    
    function = [
        {
            'name': 'generate_child_planet_report',
            'description': f"Strategies to Enhance {planets['Name']}'s Energy for Positive Benefits: Write {planets['Name']} Placement Insights, Personalized Remedies, Daily Routine and Spiritual Practice to Strengthen the {planets['Name']}'s Energy. Explain each Daily Routine and Spiritual Practice.",
            'parameters': {
                'type': 'object',
                'properties': {
                    'strategies': {
                        'type': 'array',
                        'description': f"An array of 3 Important {planets['Name']} placement insights and Impacts on {name}'s Life with simple, easy-to-understand English based on the {name}'s {planets['Name']} position and its Significance.",
                        'items': {
                            'type': 'object',
                            'properties': {
                                'title': {
                                    'type': 'string',
                                    'description': 'The title of the strategy.'
                                },
                                'content': {
                                    'type': 'string',
                                    'description': 'The explanation of the insights.'
                                }
                            },
                            'required': [
                                'title',
                                'content'
                            ]
                        }
                    },
                    'remedies': {
                        'type': 'array',
                        'description': f"An array of 3 Personalized Modern Remedies techniques with Life Skills Teachings, Food & Diet, with their names and how to implement them with guided execution steps in simple, easy-to-understand English based on the {name}'s {planets['Name']} position.",
                        'items': {
                            'type': 'object',
                            'properties': {
                                'title': {
                                    'type': 'string',
                                    'description': 'The title of the remedy.'
                                },
                                'content': {
                                    'type': 'string',
                                    'description': 'The explanation of the remedy.'
                                }
                            },
                            'required': [
                                'title',
                                'content'
                            ]
                        }
                    },
                    'routine': {
                        'type': 'array',
                        'description': f"An array of 3 Daily Mindful Routines & Rituals techniques with their names and how to implement them with guided execution steps in simple, easy-to-understand English based on the {name}'s {planets['Name']} position.",
                        'items': {
                            'type': 'object',
                            'properties': {
                                'title': {
                                    'type': 'string',
                                    'description': 'The title of the routine.'
                                },
                                'content': {
                                    'type': 'string',
                                    'description': 'The explanation of the routine.'
                                }
                            },
                            'required': [
                                'title',
                                'content'
                            ]
                        }
                    },
                    'practice': {
                        'type': 'array',
                        'description': f"An array of 3 Personalized Spiritual Practices with Mantra, Mudra, and Sacred Sounds that positively activate {planets['Name']} energy. Explain their names and how to do them with guided execution steps in simple, easy-to-understand English based on the {name}'s {planets['Name']} position.",
                        'items': {
                            'type': 'object',
                            'properties': {
                                'title': {
                                    'type': 'string',
                                    'description': 'The title of the practice.'
                                },
                                'content': {
                                    'type': 'string',
                                    'description': 'The explanation of the practice.'
                                }
                            },
                            'required': [
                                'title',
                                'content'
                            ]
                        }
                    }
                },
                'required': [
                    'strategies',
                    'remedies',
                    'routine',
                    'practice'
                ]
            }
        }
    ]
    function_call = {"name": "generate_child_planet_report"}
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": content}
        ],
        functions=function,
        function_call=function_call
    )
    
    function_response = response.choices[0].message.function_call.arguments

    res_json = json.loads(function_response)
    
    print(res_json,"\n")
    
    return res_json
    