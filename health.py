from dasa import calculate_dasa
from datetime import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)

def cutString(text):
    start_index = text.find('{')
    end_index = text.rfind('}')

    json_substring = text[start_index:end_index + 1]
    return json_substring

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

zodiac =  ["Aries","Taurus" ,"Gemini","Cancer","Leo","Virgo","Libra" ,"Scorpio" ,"Sagittarius" ,"Capricorn","Aquarius","Pisces"]

zodiac_lord = ["Mars","Venus","Mercury","Moon","Sun","Mercury","Venus","Mars","Jupiter","Saturn", "Saturn","Jupiter"]

def secondHouse(planets,shifted_signs,house):
    HousePLanet = list(filter(lambda x:x['pos_from_asc'] == house,planets))
    HouseLord = list(filter(lambda x : x['Name'] == zodiac_lord[zodiac.index(shifted_signs[house - 1])], planets))[0]
    HouseLordPLanet = list(filter(lambda x:x['pos_from_asc'] == HouseLord['pos_from_asc'],planets))
    
    prompt = f"Child's {number_words[house]} house is {shifted_signs[house - 1]} "
    
    
    if len(HousePLanet) == 1:
            prompt += f"PLanet {HousePLanet[0]['Name']} placed in {number_words[house]} house "
    elif len(HousePLanet) > 1:    
        prompt += "Planets "
        for pl in HousePLanet:
            prompt += f"{pl['Name']} "
            
            if HousePLanet.index(pl) != len(HousePLanet) - 1:
                prompt += "and "
                
        prompt += "and "
                
    else:
        prompt += ""
                
    prompt += f"and {number_words[house]} house Lord {zodiac_lord[zodiac.index(shifted_signs[house - 1])]} placed in {HouseLord['pos_from_asc']} House of {HouseLord['sign']} "
    
    HouseLordPLanet.remove(HouseLord)
    
    if len(HouseLordPLanet) == 1:
        prompt += f"along with Planet {HouseLordPLanet[0]['Name']} placed in {HouseLord['pos_from_asc']} House of {HouseLord['sign']} "
    
    if len(HouseLordPLanet) > 1:
        prompt += "along with Planets "
        for pl in HouseLordPLanet:
            prompt += f"{pl['Name']} "
            if HouseLordPLanet.index(pl) != len(HouseLordPLanet) - 1:
                prompt += "and "

    return prompt

def lagnaPrompt(planets):
    asc = list(filter(lambda x:x['Name'] == "Ascendant" , planets))[0]
    ascLord = list(filter(lambda x:x['Name'] == asc['zodiac_lord'], planets))[0]
    firstHousePLanet = list(filter(lambda x:x['pos_from_asc'] == 1,planets))
    ascLordHousePLanet = list(filter(lambda x:x['pos_from_asc'] == ascLord['pos_from_asc'],planets))
    prompt = f"Child's lagna is {asc['sign']} "
    
    if len(firstHousePLanet) == 2:
            prompt += f"PLanet {firstHousePLanet[0]['Name']} placed in lagna "
    elif len(firstHousePLanet) > 1:    
        prompt += "Planets "
        for pl in firstHousePLanet:
            if pl['Name'] == "Ascendant":
                prompt += "Placed in Lagna "
                continue
            prompt += f"{pl['Name']} "
            
            if len(firstHousePLanet) > 2 and firstHousePLanet.index(pl) != len(firstHousePLanet) - 1:
                prompt += "and "
                
        prompt += "and "
                
        for pl in firstHousePLanet:
            if pl['Name'] == "Ascendant":
                continue
            prompt += f"PLanet {pl['Name']} placed in lagna "
            if len(firstHousePLanet) > 2 and firstHousePLanet.index(pl) != len(firstHousePLanet) - 1:
                prompt += "and "
    else:
        prompt += ""
                
    prompt += f"and Lagna Lord {ascLord['Name']} placed in {ascLord['pos_from_asc']} House of {ascLord['sign']} in {ascLord['nakshatra']} Nakshatra "
    
    ascLordHousePLanet.remove(ascLord)
    
    if len(ascLordHousePLanet) == 1:
        prompt += f"along with Planet {ascLordHousePLanet[0]['Name']} "
    
    if len(ascLordHousePLanet) > 1:
        prompt += "along with Planets "
        for pl in ascLordHousePLanet:
            if pl['Name'] == ascLord['Name']:
                continue
            prompt += f"{pl['Name']} "
            if len(ascLordHousePLanet) > 2 and ascLordHousePLanet.index(pl) != len(ascLordHousePLanet) - 1:
                prompt += "and "
                
    return prompt

def planetPrompt(name):
    prompt = f"The {name['Name']} positioned in the {name['pos_from_asc']} house of {name['sign']} in {name['nakshatra']} nakshatra"
                
    return prompt

def healthPrompt(planets,index,name,gender):
    prompt = ""
    asc = list(filter(lambda x:x['Name'] == "Ascendant" , planets))[0]
    asc_index = zodiac.index(asc['sign'])
    moon = list(filter(lambda x:x['Name'] == "Moon",planets))[0]
    shifted_signs = zodiac[asc_index:] + zodiac[:asc_index]
    nakshatraLord = list(filter(lambda x:x['Name'] == moon['nakshatra_lord'],planets))[0]
    rasiLord = list(filter(lambda x:x['Name'] == moon['zodiac_lord'],planets))[0]
    
    if index == 0:
        content = f"""Create a detailed Health report for a {name} whose Astrology Details: Child's Janma Nakshatra is {moon['nakshatra']} Nakshatra and  Nakshatra Lord {nakshatraLord['Name']} placed in the {nakshatraLord['pos_from_asc']} House of {nakshatraLord['sign']} in {nakshatraLord['nakshatra']} Nakshatra.Child's Janma Rashi is {moon['sign']} Rashi and  the Rashi Lord {rasiLord['Name']} placed in the {rasiLord['pos_from_asc']} House of {rasiLord['sign']} in {rasiLord['nakshatra']} Nakshatra. {lagnaPrompt(planets)} {secondHouse(planets,shifted_signs,2)} {secondHouse(planets,shifted_signs,3)} {secondHouse(planets,shifted_signs,4)} {secondHouse(planets,shifted_signs,5)} {secondHouse(planets,shifted_signs,6)} {secondHouse(planets,shifted_signs,7)} {secondHouse(planets,shifted_signs,8)} {secondHouse(planets,shifted_signs,9)} {secondHouse(planets,shifted_signs,10)} {secondHouse(planets,shifted_signs,11)} {secondHouse(planets,shifted_signs,12)}.use {name} and {gender} pronouns all over the content."""
        
        function = [
            {
            "name": "generate_child_health_report",
        "description": f"Provide holistic wellness solutions and techniques for the {name}'s health and wellness, addressing potential health challenges related to Sun, Moon planets, 6 house Sign, 8 House Sign and 12 House signs. Write 5 natural remedies Insights  and their names and how to do them with guided execution steps, 5 nutrition tips Insights  with nutritional needs for potential health challenges, including the Nutritions  names and their  explanations of how to implement them . Also, provide 5 Spiritual Practices including Rituals, Sacred Sounds, Yoga Asanas and its names and how to do them with guided execution steps  and 3 Life Skills Teaching suggestions with actionable techniques and Its names and how to do them with guided execution steps Detail Explanations About How Implement those Life Skills  Suggestions to resolve the potential health challenges Insights  Write Each  Wellness Solutions in Separate Lines with Headline and Explanations Insights",
        "parameters": {
            "type": "object",
            "properties": {
                "health_insights": {
                    "type": "string",
                    "description": f"Explain {name}'s Health Stats Including Vada, Pitta, Kapa, and Five Elements Compositions Insights    Based on {name}’s lagna Sign,Sun,Moon Sign, 6th House Sign,8 House Sign,12th House Sign and Placements and Planets Influences Write {name}’s Health Insights Justifications Based on Health Houses and Its Elements  in Abstract Paragraph"
                },
                "challenges": {
                    "type": "array",
                    "description": f"Write {name}'s Potential Health Challenges Insights  Based on {name}'s  Ascendant Sign, Sun, Moon Signs, 6th  House Sign, 8th House Sign , 12th  House Sign and Planets  placements and influences in Health Houses  Write Potential Health Challenges Insights  in Details Explanations based on Health Astrology  Insights  Content in Separate Lines with Headline and Explanations Insights  Write Min 5 Potential Health Challenges Insights in array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the challenge."
                            },
                            "content": {
                                "type": "string",
                                "description": "The explanation of the challenge."
                            }
                        },
                        "required": ["title", "content"]
                    }
                },
                "natural_remedies": {
                    "type": "array",
                    "description": f"5 natural remedies Insights and their names and how to do them with guided execution steps based on Holistic Wellness Solutions in an array",
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
                },
                "nutrition_tips": {
                    "type": "array",
                    "description": f"5 nutrition tips Insights  with nutritional needs for potential health challenges, and its names and how to do them with guided execution steps   based on Holistic Wellness Solutions in an array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the tip."
                            },
                            "content": {
                                "type": "string",
                                "description": "The explanation of the tip."
                            }
                        },
                        "required": ["title", "content"]
                    }
                },
                "wellness_routines": {
                    "type": "array",
                    "description": f"provide 5 Spiritual Practices including Energy Healing, Sacred Sounds, Mudras and its names and how to do them with guided execution steps based on Holistic Wellness Solutions in an array'",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the routine."
                            },
                            "content": {
                                "type": "string",
                                "description": "The explanation of the routine."
                            }
                        },
                        "required": ["title", "content"]
                    }
                },
                "lifestyle_suggestions": {
                    "type": "array",
                    "description": f"3 Life Skills Teaching suggestions with actionable techniques and Its names and how to do them with guided execution steps based on Holistic Wellness Solutions in an array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the suggestion."
                            },
                            "content": {
                                "type": "string",
                                "description": "The explanation of the suggestion."
                            }
                        },
                        "required": ["title", "content"]
                    }
                },
                "preventive_tips": {
                    "type": "array",
                    "description": f"Write  preventive measures and precautions for {name}'s  health and wellness-related Challenges  based on the {name}'s Astrology health Houses Sign Write Insights Write Min 3 Preventive & Precautions in array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the suggestion."
                            },
                            "content": {
                                "type": "string",
                                "description": "The explanation of the suggestion."
                            }
                        },
                        "required": ["title", "content"]
                    }
                },
            },
            "required": ["health_insights", "challenges","natural_remedies", "nutrition_tips", "wellness_routines", "lifestyle_suggestions","preventive_tips"]
        }
    }
    ]
        function_call = {"name": "generate_child_health_report"}
            
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

