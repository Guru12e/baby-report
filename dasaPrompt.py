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

def findDifference(birthYear, birthMonth, dasaStartYear, dasaStartMonth, dasaEndYear, dasaEndMonth):
    if dasaStartYear < birthYear or (dasaStartYear == birthYear and dasaStartMonth < birthMonth):
        startYears, startMonths = 0, 0
    else:
        startYears = dasaStartYear - birthYear
        startMonths = dasaStartMonth - birthMonth
        if startMonths < 0:  
            startYears -= 1
            startMonths += 12
        
    endYears = dasaEndYear - birthYear
    endMonths = dasaEndMonth - birthMonth
    if endMonths < 0:  
        endYears -= 1
        endMonths += 12

    return startYears, startMonths,endYears, endMonths

def dasaPrompt(date_str,planets,dasa,name,gender):
    year = date_str
    today = datetime.now().year
    month = datetime.now().month
    AgeDasa = []
    
    if today - year <= 3:
        start = today
        end = today + 5
    else:
        start = today - 2
        end = today + 3
        
    for d,b in dasa.items():
        for c in b:
            if start <= c['start_year'] <= end or start <= c['end_year'] <= end:
                if start == c['end_year'] :
                    if c['end_month'] >= month:
                        AgeDasa.append({
                            "Dasa" : d,
                            "Bhukthi" : c['bhukthi'],
                            "Age" : f"At {name}'s age, Between {c['start_year'] - date_str} to {c['end_year'] - date_str}",
                        })
                else:
                    AgeDasa.append({
                        "Dasa" : d,
                        "Bhukthi" : c['bhukthi'],
                        "Age" : f"At {name}'s age, Between {c['start_year']  - date_str} to {c['end_year']  - date_str}",
                    })
                    
    dataOut = []
        
    for d in AgeDasa:
        zodiacLord = list(filter(lambda x: x['Name'] == planets[-1]['zodiac_lord'],planets))[0]
        dasa = list(filter(lambda x: x['Name'] == d['Dasa'],planets))[0]
        bhukthi = list(filter(lambda x: x['Name'] == d['Bhukthi'],planets))[0]
               
        content = (
            f"Create a detailed Dasa Bhukthi Insights report for a {name} based on the following planetary placements: "
            f"Lagna: {planets[-1]['sign']} Lagna with Lagna Lord {planets[-1]['zodiac_lord']} in the {zodiacLord['pos_from_asc']} house of {zodiacLord['sign']} in {zodiacLord['nakshatra']} Nakshatra. "
            f"Moon Placed in the {planets[1]['pos_from_asc']} house of {planets[1]['sign']}, Janma Rashi in {planets[1]['nakshatra']} Nakshatra. "
            f"Dasa & Bhukti Lords: {d['Dasa']} Dasa and {d['Bhukthi']} Bhukti. Dasa lord {d['Dasa']} is in the {dasa['pos_from_asc']}th house of {dasa['sign']} in {dasa['nakshatra']} Nakshatra, "
            f"and bhukthi Lord {bhukthi['Name']} is in the {bhukthi['pos_from_asc']} house of {bhukthi['sign']} in {bhukthi['nakshatra']} Nakshatra. "
            f"Use {name} and {gender} pronoun throughout the content."
        )

        function = [
            {
                "name": "generate_dasa_report",
                "description": f"Generate detailed insights for the {d['Dasa']} Dasa and {d['Bhukthi']} Bhukti period based on the {name}'s Lagna sign, Moon sign, Nakshatra, Dasa lord's position, and Bhukti lord's position in the {name}'s birth chart.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "insights": {
                            "type": "string",
                            "description": f"Provide {d['Dasa']} Dasa and {d['Bhukthi']} Bhukti predictions based on the Lagna sign, Moon sign, planetary placements of  Dasa Planet {d['Dasa']} and  Bukthi Planet {d['Bhukthi']}. Focus on {name}'s life events insights  such as the impacts of Dasa and Bhukti on {name}'s  life. Use concise and easy-to-understand language, avoiding technical astrology terms. The content should be a single paragraph of approximately 150 words."
                        },
                        "challenges": {
                            "type": "array",
                            "description": (
                                f"Highlight {name}'s 3 potential Life challenges and negative effects the {name} may face during the {d['Dasa']} Dasa and {d['Bhukthi']} Bhukti period and Based on {d['Dasa']} Dasa and {d['Bhukthi']} Planets Positions at {name}'s current Age "
                            ),
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "description": "The title of the challenge."
                                    },
                                    "content": {
                                        "type": "string",
                                        "description": "The detailed explanation of the challenge."
                                    }
                                },
                                "required": ["title", "content"]
                            }
                        },
                        "precautions": {
                            "type": "array",
                            "description": (
                                f"Provide 2 practical Parenting steps that parents can take to help the {name} navigate the challenges during this {d['Dasa']} Dasa and {d['Bhukthi']} Bhukti period Including Life Skills Teachings, Smart Nurturing Parenting Strategies .Explain their names and how to do them with guided execution steps in simple, easy-to-understand English."
                            ),
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "description": "The title of the precaution."
                                    },
                                    "content": {
                                        "type": "string",
                                        "description": "The detailed explanation of the precaution."
                                    }
                                },
                                "required": ["title", "content"]
                            }
                        },
                        "remedies": {
                            "type": "array",
                            "description": f"Provide 3 actionable remedies and recommendations for this {d['Dasa']} Dasa and {d['Bhukthi']} Bhukti period, focusing on real-life improvements. Include Mindful Habits building , Food & Diets ,  Spiritual Mantras & Sacred Sounds  to Mitigate the {name}'s {d['Dasa']} Dasa and {d['Bhukthi']} Bhukti challenges. Explain Actionable remedies  names and how to do them with guided execution steps in simple, easy-to-understand English",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "description": "The title of the remedy."
                                    },
                                    "content": {
                                        "type": "string",
                                        "description": "The detailed explanation of the remedy."
                                    }
                                },
                                "required": ["title", "content"]
                            }
                        }
                    },
                    "required": ["insights", "challenges", "precautions", "remedies"]
                }
            }
        ]

        function_call = {"name": "generate_dasa_report"}
       
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
        
        dataOut.append({
            "dasa" : d['Dasa'],
            "bhukthi" : d['Bhukthi'],
            "age" : d['Age'],
            "prediction" : res_json,
        })
        
        
        
    print(dataOut,"\n")
    return dataOut
