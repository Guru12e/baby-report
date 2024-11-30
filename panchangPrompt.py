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
        content = f"Create a detailed report for {name}, who was born on {panchang['paksha']} Paksha {panchang['thithi']}. use {name} and {gender} pronouns all over the content."

        function = [
            {
                "name": "generate_child_thithi_report",
                "description": f"Generate a report for {name}'s Thithi with personality traits, emotional state, life challenges, and actionable remedies.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "child_thithi_insights": {
                            "type": "string",
                            "description": f"Explain {name}'s birth Thithi characteristics, including personality traits and emotional/mental state, in a short abstract paragraph."
                        },
                        "life_challenges": {
                            "type": "string",
                            "description": "Explain the child's Thithi life challenges in a single paragraph, highlighting the potential difficulties."
                        },
                        "actionable_remedies": {
                            "type": "array",
                            "description": "An array of 2 personalized and effective remedies for Thithi  Spiritual Practice, Daily Ritual & Routine, Life Skills teaching with their names and How to do them with Guided Execution Steps for these remedies to mitigate  the Thithi-related challenges. Avoid suggestions like consulting an astrologer or healer, focus only on practical and guided solutions.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "description": "The title of the remedy."
                                    },
                                    "content": {
                                        "type": "string",
                                        "description": "The explanation of the remedy."
                                    }
                                },
                                "required": ["title", "content"]
                            }
                        }
                    },
                    "required": ["child_thithi_insights", "life_challenges", "actionable_remedies"]
                }
            }
        ]


        function_call = {"name": "generate_child_thithi_report"}
        
    if index == 1:
        content = f"Create a detailed report for {name}, who was born on {panchang['week_day']}.use {name} and {gender} pronouns all over the content."

        function = [
            {
                "name": "generate_child_varam_report",
                "description": f"Generate a report for {name}'s birth Vaaram, including characteristics, life challenges, and actionable remedies.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "child_week_insights": {
                            "type": "string",
                            "description": (
                                f"Describe {name}'s birth Vaaram characteristics, such as unique traits and their impact on the child's life, in a short paragraph."
                            )
                        },
                        "life_challenges": {
                            "type": "string",
                            "description": (
                                f"Highlight the potential challenges associated with {name}'s birth Vaaram in a single paragraph."
                            )
                        },
                        "actionable_remedies": {
                            "type": "array",
                            "description": "An array of 3 personalized and effective remedies for Vaaram  Spiritual Practice, Holistics Wellness Routine , Mantras & Sacred Sound with their names and How to do them with Guided Execution Steps for these remedies to mitigate  the Vaaram -related challenges. Avoid suggestions like consulting an astrologer or healer; focus only on practical and guided solutions Avoid suggestions like consulting an astrologer, coach, or healer",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "description": "The title of the remedy."
                                    },
                                    "content": {
                                        "type": "string",
                                        "description": "A detailed explanation of the remedy."
                                    }
                                },
                                "required": ["title", "content"]
                            }
                        }
                    },
                    "required": ["child_week_insights", "life_challenges", "actionable_remedies"]
                }
            }
        ]


        
        function_call = {"name": "generate_child_varam_report"}
        
    if index == 2:
        content = f"Create a detailed report for {name}, who was born under the {panchang['nakshatra']} Nakshatra.use {name} and {gender} pronouns all over the content."

        function = [
            {
                "name": "generate_child_nakshatra_report",
                "description": f"Generate a report explaining {name}'s Nakshatra characteristics, life challenges, and actionable remedies.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "child_nakshatra_insights": {
                            "type": "string",
                            "description": (
                                f"Provide insights into {name}'s Nakshatra characteristics, including personality traits and life path, in a short paragraph."
                            )
                        },
                        "life_challenges": {
                            "type": "string",
                            "description": (
                                f"Highlight potential life challenges associated with {name}'s birth Nakshatra in a single paragraph."
                            )
                        },
                        "actionable_remedies": {
                            "type": "array",
                            "description": "An array of 3 personalized and effective remedies for birth Nakshatra Including GOd Worship, Mantras & Sacred Sound, Exercise & Asanas  with their names and How to do them with Guided Execution Steps for these remedies to mitigate  the Nakshatra related challenges. Avoid suggestions like consulting an astrologer or healer, focus only on practical and guided solutions Avoid suggestions like consulting an astrologer, coach, or healer.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "description": "The title of the remedy."
                                    },
                                    "content": {
                                        "type": "string",
                                        "description": "A detailed explanation of the remedy."
                                    }
                                },
                                "required": ["title", "content"]
                            }
                        }
                    },
                    "required": ["child_nakshatra_insights", "life_challenges", "actionable_remedies"]
                }
            }
        ]

        function_call = {"name": "generate_child_nakshatra_report"}
    if index == 3:
        content = f"Create a detailed report for {name}, who was born under the {panchang['yoga']} Yogam.use {name} and {gender} pronouns all over the content."

        function = [
            {
                "name": "generate_child_yogam_report",
                "description": f"Generate a detailed report explaining {name}'s Yogam characteristics, life challenges, and actionable remedies.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "child_yogam_insights": {
                            "type": "string",
                            "description": (
                                f"Provide insights into {name}'s Yogam characteristics, including goals, spiritual growth, and overall impact, in a short paragraph."
                            )
                        },
                        "life_challenges": {
                            "type": "string",
                            "description": (
                                f"Describe potential life challenges associated with {name}'s Yogam in a single paragraph."
                            )
                        },
                        "actionable_remedies": {
                            "type": "array",
                            "description": f"Provide an array of 2 personalized, effective remedies for challenges related to the {name}'s Yogam. Focus on lifestyle changes, holistic wellness, energy healing, and spiritual remedies with their names and How to do them with Guide Execution Steps. Avoid suggesting consulting an astrologer, coach, or healer.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "description": "The title of the remedy."
                                    },
                                    "content": {
                                        "type": "string",
                                        "description": "A detailed explanation of the remedy."
                                    }
                                },
                                "required": ["title", "content"]
                            }
                        }
                    },
                    "required": ["child_yogam_insights", "life_challenges", "actionable_remedies"]
                }
            }
        ]


        function_call = {"name": "generate_child_yogam_report"}
        
    if index == 4:
        content = f"Create a detailed report for {name}, who was born under the {panchang['karanam']} Karanam.use {name} and {gender} pronouns all over the content."

        function = [
            {
                "name": "generate_child_karanam_report",
                "description": f"Generate a detailed report explaining {name}'s Karanam characteristics, life challenges, and actionable remedies.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "child_karanam_insights": {
                            "type": "string",
                            "description": (
                                f"Provide insights into {name}'s Karanam characteristics, including approaches to tasks, work habits, success strategies, and achievements, in a short paragraph."
                            )
                        },
                        "life_challenges": {
                            "type": "string",
                            "description": (
                                f"Describe potential life challenges associated with {name}'s Karanam in a single paragraph."
                            )
                        },
                        "actionable_remedies": {
                            "type": "array",
                            "description": f"Provide an array of 3 personalized, effective remedies for challenges related to the {name}'s Karanam. Focus on lifestyle changes, holistic wellness, energy healing, spiritual remedies, and mindfulness techniques. Include detailed explanations and step-by-step guidance for implementation. Avoid suggesting consulting an astrologer, coach, or healer",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "description": "The title of the remedy."
                                    },
                                    "content": {
                                        "type": "string",
                                        "description": "A detailed explanation of the remedy."
                                    }
                                },
                                "required": ["title", "content"]
                            }
                        }
                    },
                    "required": ["child_karanam_insights", "life_challenges", "actionable_remedies"]
                }
            }
        ]

        function_call = {"name": "generate_child_karanam_report"}
      
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
