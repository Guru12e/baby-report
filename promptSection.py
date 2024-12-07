from openai import OpenAI
import os
from dotenv import load_dotenv
import json
import datetime

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
zodiac =  ["Aries","Taurus" ,"Gemini","Cancer","Leo","Virgo","Libra" ,"Scorpio" ,"Sagittarius" ,"Capricorn","Aquarius","Pisces"]

zodiac_lord = ["Mars","Venus","Mercury","Moon","Sun","Mercury","Venus","Mars","Jupiter","Saturn", "Saturn","Jupiter"]

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

def firstHouse(planets):
    sun = list(filter(lambda x:x['Name'] == "Sun",planets))[0]
    moon = list(filter(lambda x:x['Name'] == "Moon",planets))[0]
    
    prompt = lagnaPrompt(planets)
    
    prompt += ","
    
    prompt += planetPrompt(sun)
    
    prompt += ", "
    
    prompt += planetPrompt(moon)

    return prompt

def physical(planets,index,name,gender):
    if index == 1:
        prompt = "Provide Child's Physical Attribute Insights in Paragraph "
        
        prompt += lagnaPrompt(planets)
    
        prompt += "Write Physical Attributes Insights Child's Body Built, Face Type , Eyes, Physical Appearance, Aura in Detail Explanations Paragraph Do not Explain Planetary Position Details Solely explain the content"
    
    if index == 2 :
        moon = list(filter(lambda x:x['Name'] == "Moon" , planets))[0]
        nakshatraLord = list(filter(lambda x:x['Name'] == moon['nakshatra_lord'], planets))[0]
        rasiLord = list(filter(lambda x:x['Name'] == moon['zodiac_lord'], planets))[0]
        asc = list(filter(lambda x:x['Name'] == "Ascendant" , planets))[0]
        asc_index = zodiac.index(asc['sign'])
        shifted_signs = zodiac[asc_index:] + zodiac[:asc_index]
        content = f"""Create a detailed Outer Personality report for a {name} whose Astrology Details: Child's Janma Nakshatra is  {moon['nakshatra']} Nakshatra and  Nakshatra Lord {nakshatraLord['Name']} placed in the {nakshatraLord['pos_from_asc']} House of {nakshatraLord['sign']} in {nakshatraLord['nakshatra']} Nakshatra. Child's Janma Rashi is {moon['sign']} Rashi and the Rashi Lord {rasiLord['Name']} placed in the {rasiLord['pos_from_asc']} House of {rasiLord['sign']} in {rasiLord['nakshatra']} Nakshatra. {lagnaPrompt(planets)} {secondHouse(planets,shifted_signs,2)} {secondHouse(planets,shifted_signs,3)} {secondHouse(planets,shifted_signs,4)} {secondHouse(planets,shifted_signs,5)} {secondHouse(planets,shifted_signs,6)} {secondHouse(planets,shifted_signs,7)} {secondHouse(planets,shifted_signs,8)} {secondHouse(planets,shifted_signs,9)} {secondHouse(planets,shifted_signs,10)} {secondHouse(planets,shifted_signs,11)} {secondHouse(planets,shifted_signs,12)}.Use {name} and {gender} pronouns all over the content."""
        
        function = function = [
  {
    'name': 'generate_child_outer_personality_report',
    'description': f"Generate a detailed report on the {name}'s character, behavior, and qualities based on astrological insights. This includes insights into the {name}'s Lagna (Ascendant), Lagna Lord placements, and other key planetary and house positions.The report will include 3 character insights, 3 behavior insights, 3  negative personality impacts ",
    'parameters': {
      'type': 'object',
      'properties': {
        'outer_personality': {
          'type': 'string',
          'description': f"Provide a brief explanation of the {name}'s outer personality, including physical attributes and outward persona, based on the {name}'s astrological details (Lagna and Lagna Lord placements)."
        },
        'character': {
          'type': 'array',
          'description': f"Provide 3 insights into the {name}'s character, explained in simple and easy-to-understand language, based on the {name}'s astrological details (Lagna, planets, and house placements). Each insight should include a title and detailed explanation.",
          'items': {
            'type': 'object',
            'properties': {
              'title': {
                'type': 'string',
                'description': 'The title of the character insight.'
              },
              'content': {
                'type': 'string',
                'description': 'A detailed explanation of the character insight.'
              }
            },
            'required': ['title', 'content']
          }
        },
        'behaviour': {
          'type': 'array',
          'description': f"Provide 3 insights into the {name}'s behavior, explained in simple language, based on astrological details such as Lagna and planetary house placements. Each insight should be accompanied by a title and detailed explanation.",
          'items': {
            'type': 'object',
            'properties': {
              'title': {
                'type': 'string',
                'description': 'The title of the behavior insight.'
              },
              'content': {
                'type': 'string',
                'description': 'A detailed explanation of the behavior insight.'
              }
            },
            'required': ['title', 'content']
          }
        },
        'negative_impact': {
          'type': 'array',
          'description': f"Provide an array of 3 negative personality or behavior traits that may affect the {name}'s overall development. Include insights into areas for improvement, based on astrological placements. Each trait should be explained with its title and content.",
          'items': {
            'type': 'object',
            'properties': {
              'title': {
                'type': 'string',
                'description': 'The title of the negative impact.'
              },
              'content': {
                'type': 'string',
                'description': 'A detailed explanation of the negative impact.'
              }
            },
            'required': ['title', 'content']
          }
        },
      },
      'required': ['outer_personality', 'character', 'behaviour', 'negative_impact']
    }
  }
]
        function_call = {"name": "generate_child_outer_personality_report"}
        
    if index == 3:
        moon = list(filter(lambda x:x['Name'] == "Moon" , planets))[0]
        nakshatraLord = list(filter(lambda x:x['Name'] == moon['nakshatra_lord'], planets))[0]
        rasiLord = list(filter(lambda x:x['Name'] == moon['zodiac_lord'], planets))[0]
        asc = list(filter(lambda x:x['Name'] == "Ascendant" , planets))[0]
        asc_index = zodiac.index(asc['sign'])
        shifted_signs = zodiac[asc_index:] + zodiac[:asc_index]
        content = f"""Create a detailed Inner Personality report for a {name} whose Astrology Details: Child's Janma Nakshatra is  {moon['nakshatra']} Nakshatra and  Nakshatra Lord {nakshatraLord['Name']} placed in the {nakshatraLord['pos_from_asc']} House of {nakshatraLord['sign']} in {nakshatraLord['nakshatra']} Nakshatra. Child's Janma Rashi is {moon['sign']} Rashi and the Rashi Lord {rasiLord['Name']} placed in the {rasiLord['pos_from_asc']} House of {rasiLord['sign']} in {rasiLord['nakshatra']} Nakshatra. {lagnaPrompt(planets)} {secondHouse(planets,shifted_signs,2)} {secondHouse(planets,shifted_signs,3)} {secondHouse(planets,shifted_signs,4)} {secondHouse(planets,shifted_signs,5)} {secondHouse(planets,shifted_signs,6)} {secondHouse(planets,shifted_signs,7)} {secondHouse(planets,shifted_signs,8)} {secondHouse(planets,shifted_signs,9)} {secondHouse(planets,shifted_signs,10)} {secondHouse(planets,shifted_signs,11)} {secondHouse(planets,shifted_signs,12)}.Use {name} and {gender} pronouns all over the content."""
        
        function = [
  {
    'name': 'generate_child_inner_personality_report',
    'description': f"Generate a detailed report on the {name}'s inner personality, emotional needs, thoughts, beliefs, feelings, reactions, and emotional stability based on the {name}'s Moon Sign and other relevant astrological placements. The report will include 3  insights each for emotional needs, thoughts & beliefs, feelings & reactions, and emotional stability",
    'parameters': {
      'type': 'object',
      'properties': {
        'inner_worlds': {
          'type': 'string',
          'description': f"Provide a brief overview of the {name}'s emotional needs, including insights into {name}'s core emotional world, based on {name}'s astrological details such as Moon Sign and other planetary placements."
        },
        'emotional_needs': {
          'type': 'array',
          'description': f"Provide 3 insights into the {name}'s emotional needs, explained in simple and easy-to-understand language. Each insight should be based on the {name}'s astrological details (Moon Sign, planets, and house placements). Include a title and detailed explanation for each insight.",
          'items': {
            'type': 'object',
            'properties': {
              'title': {
                'type': 'string',
                'description': 'The title of the emotional need insight.'
              },
              'content': {
                'type': 'string',
                'description': 'A detailed explanation of the emotional need insight.'
              }
            },
            'required': ['title', 'content']
          }
        },
        'impact': {
          'type': 'array',
          'description': f"Provide an array of negative emotions and feelings that could impact the {name}'s overall development. Each negative trait should be explained, along with the areas that need improvement for emotional growth. The insights should be based on the {name}'s astrological influences.",
          'items': {
            'type': 'object',
            'properties': {
              'title': {
                'type': 'string',
                'description': 'The title of the emotional impact.'
              },
              'content': {
                'type': 'string',
                'description': 'A detailed explanation of the emotional impact.'
              }
            },
            'required': ['title', 'content']
          }
        },
      },
      'required': ['inner_worlds', 'emotional_needs', 'impact']
    }
  }
]

        function_call = {"name": "generate_child_inner_personality_report"}
    if index == 4:
      content = f"Create a detailed {name}'s core identity report for a {name} whose Lagna, Moon, and Sun sign placements are {firstHouse(planets)}.Use {name} and {gender} pronouns all over the content."
      
      function = [
        {
          'name': 'generate_child_core_identity_report',
          'description': f"Analyze the {name}'s core identity,and how {name} balance strength between outer and inner personality traits based on {name}'s Lagna, Sun sign placements. This report includes insights into {name}'s recognition needs, primary motivations, sense of identity, and practical remedies for improving {name}'s core identity and overcoming challenges related to identity and ego.",
          'parameters': {
            'type': 'object',
            'properties': {
              'core_identity': {
                'type': 'string',
                'description': f"Provide an abstract overview of {name}'s core identity, ego, and how {name} balance strengths between {name}'s outer (social) and inner (self-perception) personality traits, based on {name}'s Lagna, Moon, and Sun sign placements"
                },
                'recognitions': {
                  'type': 'array',
                  'description': f"Explain the {name}'s Seek  for recognition and how {name} seek acknowledgment from others. Provide 3 insights based on {name}'s Lagna, Moon, and Sun sign placements, with clear explanations in simple terms",
                  'items': {
                    'type': 'object',
                    'properties': {
                      'title': {
                        'type': 'string',
                        'description': 'The title of the recognition insight.'
                      },
                      'content': {
                        'type': 'string',
                        'description': f'Detailed explanation of the recognition need based on the {name}’s astrological placements.'
                      }
                    },
                    'required': ['title', 'content']
                  }
                },
                'remedies': {
                  'type': 'array',
                  'description': f"Provide 3 practical, actionable remedies that help improve the {name}'s core identity, self-confidence, and ego balance with remedies names and How to do them with Guided execution steps These remedies should align with the {name}'s astrological placements (Lagna, Sun, and Moon).",
                  'items': {
                    'type': 'object',
                    'properties': {
                    'title': {
                        'type': 'string',
                        'description': 'The title of the remedy.'
                    },
                    'content': {
                        'type': 'string',
                        'description': f'Detailed explanation of each remedy, focusing on how to execute it to improve the {name}’s identity and overcome ego-related challenges.'
                    }
                    },
                    'required': ['title', 'content']
                }
              }
            },
            'required': ['core_identity', 'recognitions', 'remedies']
          }
        }
      ]


      function_call = {"name": "generate_child_core_identity_report"}
    if index == 5:
        moon = list(filter(lambda x:x['Name'] == "Moon" , planets))[0]
        nakshatraLord = list(filter(lambda x:x['Name'] == moon['nakshatra_lord'], planets))[0]
        rasiLord = list(filter(lambda x:x['Name'] == moon['zodiac_lord'], planets))[0]
        asc = list(filter(lambda x:x['Name'] == "Ascendant" , planets))[0]
        asc_index = zodiac.index(asc['sign'])
        shifted_signs = zodiac[asc_index:] + zodiac[:asc_index]
        content = f"""Create a detailed {name}'s Family Relationships and Social Development report for a {name} whose Child's Astrology Details: Child's Janma Nakshatra is  {moon['nakshatra']} Nakshatra and  Nakshatra Lord {nakshatraLord['Name']} placed in the {nakshatraLord['pos_from_asc']} House of {nakshatraLord['sign']} in {nakshatraLord['nakshatra']} Nakshatra. Child's Janma Rashi is {moon['sign']} Rashi and the Rashi Lord {rasiLord['Name']} placed in the {rasiLord['pos_from_asc']} House of {rasiLord['sign']} in {rasiLord['nakshatra']} Nakshatra. {lagnaPrompt(planets)} {secondHouse(planets,shifted_signs,2)} {secondHouse(planets,shifted_signs,3)} {secondHouse(planets,shifted_signs,4)} {secondHouse(planets,shifted_signs,5)} {secondHouse(planets,shifted_signs,6)} {secondHouse(planets,shifted_signs,7)} {secondHouse(planets,shifted_signs,8)} {secondHouse(planets,shifted_signs,9)} {secondHouse(planets,shifted_signs,10)} {secondHouse(planets,shifted_signs,11)} {secondHouse(planets,shifted_signs,12)}.Use {name} and {gender} pronouns all over the content."""

        function = [
            {
                'name': 'generate_family_and_social_report',
                'description': f"Write insights about the {name}'s social development, friendship dynamics, peer interaction, and family dynamics (relationships with parents and siblings) based on the {name}'s 11th House, 7th House, Sun (for Father), Moon (for Mother), and Venus planetary positions. Write the contents in an abstract paragraph format.",
                'parameters': {
                'type': 'object',
                'properties': {
                    'family_relationship': {
                    'type': 'string',
                    'description': f"Write {name}'s approaches for social development, friendship, relationship, peer interaction, and family dynamics like relationships with father, mother, siblings. based on the {name}'s 11th House, 7th House, Sun Positions for father , Moon Position for mother , Venus for social development ). Write the content in an abstract paragraph format."
                    },
                    'approaches': {
                    'type': 'array',
                    'description': f"Write 3 {name}'s approaches for building relationship and social development, bonding with father based on sun Sign , bonding  mother based on moon Sign, bonding with siblings, Bonding with friends . These should be based on social development and relationship astrology (11th House, 7th House, Sun, Moon, Venus planetary placements). Write the contents in array format.",
                    'items': {
                        'type': 'object',
                        'properties': {
                        'title': {
                            'type': 'string',
                            'description': 'The title of the approach.'
                        },
                        'content': {
                            'type': 'string',
                            'description': 'The explanation of the approach.'
                        }
                        },
                        'required': [
                        'title',
                        'content'
                        ]
                    }
                    },
                    'challenges': {
                    'type': 'array',
                    'description': f"Write personalized challenges that the {name} faces in social and family relationship. This includes challenges in family, friendship, and social settings, based on planetary influences. Write a minimum of 3 challenges in the array.",
                    'items': {
                        'type': 'object',
                        'properties': {
                        'title': {
                            'type': 'string',
                            'description': 'The title of the challenge.'
                        },
                        'content': {
                            'type': 'string',
                            'description': 'The explanation of the challenge.'
                        }
                        },
                        'required': [
                        'title',
                        'content'
                        ]
                    }
                    },
                    'parenting_support': {
                    'type': 'array',
                    'description': f"Write 3  personalized  parenting support Techniques  Including  life skills Teachings , Nurturing Parenting Strategies, Mindful habit building  that address the {name}'s social and family relationship development challenges. Write  Parenting support Technique name and How to Implement them with guided execution steps. Write the content related to parenting support.",
                    'items': {
                        'type': 'object',
                        'properties': {
                        'title': {
                            'type': 'string',
                            'description': 'The title of the parenting support.'
                        },
                        'content': {
                            'type': 'string',
                            'description': 'The explanation of the parenting support.'
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
                    'family_relationship',
                    'approaches',
                    'challenges',
                    'parenting_support'
                ]
                }
            }
            ]

        function_call = {"name": "generate_family_and_social_report"}

    if index == 1:
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
    
    else:
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


def chapterPrompt(planets,index,name,gender):
    asc = list(filter(lambda x:x['Name'] == "Ascendant" , planets))[0]
    asc_index = zodiac.index(asc['sign'])
    shifted_signs = zodiac[asc_index:] + zodiac[:asc_index]
    
    if index == 0:
        mercury = list(filter(lambda x:x['Name'] == "Mercury" , planets))[0]
        venus = list(filter(lambda x:x['Name'] == "Venus" , planets))[0]
        mars = list(filter(lambda x:x['Name'] == "Mars" , planets))[0]
        content = f"Create a Unique Talents Insights detailed report for a {name}'s Astrology Details : {planetPrompt(mercury)} {planetPrompt(venus)} {planetPrompt(mars)}"
        
        function = [{
  'name': 'generate_unique_talents_report',
  'description': f"Generate a report on the {name}'s unique strengths, highlighting natural inherent talents and abilities. The report is based on Mars, Venus, Mercury Planet Positions, house placement. Provide strategies to nurture these talents effectively, including practical suggestions for areas of growth and improvement, tailored to the {name}'s Mars, Venus, Mercury Positions. Use {name} and {gender} pronouns throughout the content.",
  'parameters': {
    'type': 'object',
    'properties': {
      'insights': {
        'type': 'string',
        'description': f"Provide detailed insights about the {name}'s unique talents, strengths, and inner values, based on Mars, venus, Mercury  planetary and house placements. This should be presented in an abstract paragraph that explains the {name}'s inherent qualities and potential."
      },
      'education': {
        'type': 'array',
        'description': f"Identify 5 unique talents related to the {name}'s  Mercury Positions Potential Talents along with Parenting Tips  to nurture these talents effectively . These should align with the {name}'s Planet mercury placements . Include how these talents manifest in the {name}'s mercury related  Natural Talents.",
        'items': {
          'type': 'object',
          'properties': {
            'title': {
              'type': 'string',
              'description': 'The title of the talent in education and intellect.'
            },
            'content': {
              'type': 'string',
              'description': f"A description of the {name}'s natural educational talents and intellectual strengths, based on Planet Mercury Placements."
            }
          },
          'required': ['title', 'content']
        }
      },
      'arts_creative': {
        'type': 'array',
        'description': f"Identify 5 unique talents related to the {name}'s Venus Placements Unique Talents Natural Skills  Potentials along with Parenting Tips  to nurture these talents effectively . These should be aligned with the {name}'s Venus  placements, particularly those involving Venus and creative house placements. Explain how these talents influence the {name}'s Venus related Natural Talents.",
        'items': {
          'type': 'object',
          'properties': {
            'title': {
              'type': 'string',
              'description': 'The title of the creative talent.'
            },
            'content': {
              'type': 'string',
              'description': f"A description of the {name}’s natural artistic talents and creative strengths, based on venus PLacements."
            }
          },
          'required': ['title', 'content']
        }
      },
      'physical_activity': {
        'type': 'array',
        'description': f"Identify 5 unique talents related to Planet Mars Positions .These should align with the {name}'s planet Mars placements Unique Talents & Skills  along with Parenting Tips  to nurture these talents effectively. Explain how these talents manifest in the {name}'s Marse related natural talents.",
        'items': {
          'type': 'object',
          'properties': {
            'title': {
              'type': 'string',
              'description': 'The title of the physical talent.'
            },
            'content': {
              'type': 'string',
              'description': f'A description of the {name}’s natural physical abilities and hobbies, based on astrology.'
            }
          },
          'required': ['title', 'content']
        }
      }
    },
    'required': ['insights', 'education', 'arts_creative', 'physical_activity']
  }
}
]
        function_call = {"name": "generate_unique_talents_report"}
        
    if index == 3:
        moon = list(filter(lambda x:x['Name'] == "Moon" , planets))[0]
        
        content = f"Create a Education and Intellectual Insights detailed report for a {name} for Child's Astrology Details : Child's Jenma Nakshtra is {moon['nakshatra']} Nakshtra Child's Jenma Raasi is {moon['sign']} {lagnaPrompt(planets)} {secondHouse(planets,shifted_signs,2)} {secondHouse(planets,shifted_signs,3)} {secondHouse(planets,shifted_signs,4)} {secondHouse(planets,shifted_signs,5)} {secondHouse(planets,shifted_signs,6)} {secondHouse(planets,shifted_signs,7)} {secondHouse(planets,shifted_signs,8)} {secondHouse(planets,shifted_signs,9)} {secondHouse(planets,shifted_signs,10)} {secondHouse(planets,shifted_signs,11)} {secondHouse(planets,shifted_signs,12)} Write {name} Educations & Intellect Details.Use {name} and {gender} pronouns all over the content."
        function = [
            {
            "name": "generate_child_education_report",
        "description": f"Explain {name}'s Education and Intellectual Insights based on astrology position",
        "parameters": {
            "type": "object",
            "properties": {
                "insights": {
                    "type": "string",
                    "description": f"Provide detailed explanations about the {name}'s Education and Learning Potentials Insights Based on Educations & Intellect Astrological Planets & House Placements  in Abstract Paragraph"
                },
                "suitable_educational": {
                    "type": "array",
                    "description": f"Write {name}'s 7 Suitable Educations Courses &  and disciplines for {name}'s academic excellence and  {name}'s personal satisfaction that Align with {name}'s Natural Talents and Strength and Interest Based on {name}'s Educations and Intellect Astrology Planets and Houses Placements Write Min 7 Suitable and Successful Education Courses and Fields Insights",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the insights."
                            },
                            "content": {
                                "type": "string",
                                "description": "The explanation of the insights."
                            }
                        },
                        "required": ["title", "content"]
                    }
                },
                "cognitive_abilities": {
                    "type": "array",
                    "description": f"Write {name}'s Unique Cognitive Abilities that Align with {name}'s Natural Talents and Strength, INterest Based on {name}'s Educations and Intellect Astrology Planets and Houses Placements Write Min 5 Unique Cognitive Abilities in array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the cognitive abilities."
                            },
                            "content": {
                                "type": "string",
                                "description": "The explanation of the cognitive abilities."
                            }
                        },
                        "required": ["title", "content"]
                    }
                },
                "recommendations": {
                    "type": "array",
                    "description": f"Provide 5 Personalized Learning Techniques & strategies in array to nurture {name}'s Educations Intellects that Align with {name}'s Natural Talents and Strength and Interest, Learning Preferences Based on {name}'s Educations and Intellect Astrology Planets and Houses Placements  Add practical suggestions & recommendations for paving the way for {name}'s academic excellence, skill enhancement, and {name}'s personal satisfaction based on the {name}'s Educations & Learning Intellects astrological planetary and house placements. Write Min 5 Perfect Learning Techniques with their name and How to do them with guided execution steps them Insights that paving the way for {name}'s academic excellence, skill enhancement, and personal satisfaction with Modern Techniques How to Implement it",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the recommendations."
                            },
                            "content": {
                                "type": "string",
                                "description": "The explanation of the recommendations."
                            }
                        },
                        "required": ["title", "content"]
                    }
                }
            },
            "required": ["insights", "suitable_educational", "cognitive_abilities", "recommendations"]
        }
    }
    ]
        function_call = {"name": "generate_child_education_report"}
        
    if index == 4:
        moon = list(filter(lambda x:x['Name'] == "Moon" , planets))[0]
        nakshatraLord = list(filter(lambda x:x['Name'] == moon['nakshatra_lord'], planets))[0]
        rasiLord = list(filter(lambda x:x['Name'] == moon['zodiac_lord'], planets))[0]
        content = f"""Create a Career Path Insights detailed report for a {name} for Child's Astrology Details : Child's Astrology Details: Child's Janma Nakshatra is  {moon['nakshatra']} Nakshatra and  Nakshatra Lord {nakshatraLord['Name']} placed in the {nakshatraLord['pos_from_asc']} House of {nakshatraLord['sign']} in {nakshatraLord['nakshatra']} Nakshatra. Child's Janma Rashi is {moon['sign']} Rashi and the Rashi Lord {rasiLord['Name']} placed in the {rasiLord['pos_from_asc']} House of {rasiLord['sign']} in {rasiLord['nakshatra']} Nakshatra. {lagnaPrompt(planets)} {secondHouse(planets,shifted_signs,2)} {secondHouse(planets,shifted_signs,3)} {secondHouse(planets,shifted_signs,4)} {secondHouse(planets,shifted_signs,5)} {secondHouse(planets,shifted_signs,6)} {secondHouse(planets,shifted_signs,7)} {secondHouse(planets,shifted_signs,8)} {secondHouse(planets,shifted_signs,9)} {secondHouse(planets,shifted_signs,10)} {secondHouse(planets,shifted_signs,11)} {secondHouse(planets,shifted_signs,12)}.Use {name} and {gender} pronouns all over the content."""
       
        function = [
            {
            "name": "generate_child_career_report",
        "description": f"Explain {name}'s Career path based on astrology position",
        "parameters": {
            "type": "object",
            "properties": {
                "career_path": {
                    "type": "string",
                    "description": f"Provide detailed explanations about the {name}'s Successful Suitable Career path  and Business Potentials Insights and derived {name}'s Fulfilled Career choice Provide conclusions about career and Business Potentials  Based on 10th House lord Placements and Planets Placed in the 10th House and 2nd House lord Placements and Planets Placed in the 2nd House and Career Astrological Planets Positions & House Placements Comprehensive Analysis insights in Abstract Paragraph"
                },
                "suitable_professions": {
                    "type": "array",
                    "description": f"Write {name}'s Successful Suitable Ideal Career Path & Professions that Align with {name}'s Natural Talents Abilities and Strength and Interest Based on {name}'s Career Astrology  Planets and 10th House 6th House  Career Houses Compressive Insights That  helping {name} achieve success and fulfillment in their professional Career  Write Min 7 Suitable and Successful Career Path & Designations and its Sectors and Fields insights with justification content in Headline Followed by Its Explanations Paragraph",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the professions."
                            },
                            "content": {
                                "type": "string",
                                "description": "The explanation of the professions."
                            }
                        },
                        "required": ["title", "content"]
                    }
                },
                "business": {
                    "type": "array",
                    "description": f"Write {name}'s Unique Business & Entrepreneurial Potentials that Align with {name}'s Natural Talents and Strength, Interest Based on {name}'s Business & Entrepreneurial Astrology Planets and Career Houses insights Content Write 5 Business &  Entrepreneurial Potentials with Sectors & Fields Content Insights with Justification content in Headline Followed By Short Explanations",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the business."
                            },
                            "content": {
                                "type": "string",
                                "description": "The explanation of the business."
                            }
                        },
                        "required": ["title", "content"]
                    }
                }
            },
            "required": ["career_path", "suitable_professions", "business"]
        }
    }
    ]
        function_call = {"name": "generate_child_career_report"}
        
    if index == 5:
        moon = list(filter(lambda x:x['Name'] == "Moon" , planets))[0]
        nakshatraLord = list(filter(lambda x:x['Name'] == moon['nakshatra_lord'], planets))[0]
        rasiLord = list(filter(lambda x:x['Name'] == moon['zodiac_lord'], planets))[0]
        content = f"""Create a SubConscious Mind detailed report for a {name} for Child's Astrology Details: Child's Janma Nakshatra is  {moon['nakshatra']} Nakshatra and  Nakshatra Lord {nakshatraLord['Name']} placed in the {nakshatraLord['pos_from_asc']} House of {nakshatraLord['sign']} in {nakshatraLord['nakshatra']} Nakshatra. Child's Janma Rashi is {moon['sign']} Rashi and the Rashi Lord {rasiLord['Name']} placed in the {rasiLord['pos_from_asc']} House of {rasiLord['sign']} in {rasiLord['nakshatra']} Nakshatra. {lagnaPrompt(planets)} {secondHouse(planets,shifted_signs,8)} {secondHouse(planets,shifted_signs,12)}.Use {name} and {gender} pronouns all over the content."""
               
        function = [{
    "name": "generate_child_subconscious_report",
    "description": f"Personalized affirmations, visualizations, and meditation techniques for parents to help {name} overcome limiting beliefs, Self Esteem, hidden fears, Deep Rooted Anxiety in their subconscious mind. This is based on Lagana Lord, 8th House, 12 house  planetary positions,  and the influence of the Moon for cultivating positive beliefs and ensuring success. Provide 5 personalized affirmations, 5 visualization techniques, and 5 meditation techniques, including names and implementation steps, to aid {name}'s growth and help them overcome subconscious mind obstacles.",
    "parameters": {
        "type": "object",
        "properties": {
            "subconscious_mind": {
                "type": "string",
                "description": f"Provide insights into {name}'s subconscious mind limiting belief , Self Esteem Issues, Hidden Fears, Deep Rooted Anxiety explaining the {name}'s limiting beliefs, Hidden Fears, Deep Rooted Anxieties  that cause obstacles in  {name}'s Life based  subconscious mind  House Lagna Lord Positions Sign, 8 th House, 12 House Planet Placement and Moon positions."
            },
            "personalized_affirmations": {
                "type": "array",
                "description": f"Provide an array of 5 personalized affirmations to help {name} overcome limiting beliefs, Self Esteem Issues, Provide Affirmations Techniques name and How to do them with guided execution steps for each affirmation, including Affirmation Counts. These affirmation  should focus on building positive beliefs, High Self esteem for {name}'s success.",
                "items": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The title of the affirmation."
                        },
                        "content": {
                            "type": "string",
                            "description": "The explanation of the affirmation and how it can be implemented."
                        }
                    },
                    "required": ["title", "content"]
                }
            },
            "visualizations": {
                "type": "array",
                "description": f"Provide an array of 5 personalized visualization techniques for {name}'s limiting beliefs, Hidden Fears,  Provide  Visualization Techniques name and How to do them with guided execution steps for each visualization, including imaginary techniques. These techniques should focus on building positive beliefs, Removing Hidden Fears  for {name}'s success.",
                "items": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The title of the visualization technique."
                        },
                        "content": {
                            "type": "string",
                            "description": "The explanation of the visualization and how it can be implemented."
                        }
                    },
                    "required": ["title", "content"]
                }
            },
            "meditations": {
                "type": "array",
                "description": f"Provide an array of 5 personalized mindful meditation techniques for {name}'s limiting beliefs, deep rooted anxiety Provide mediation Techniques name and How to do them with guided execution steps for each mindful meditation, including counting techniques. These techniques should focus on building positive beliefs, Removing Deep Rooted Anxiety  for {name}’s success.",
                "items": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The title of the meditation technique."
                        },
                        "content": {
                            "type": "string",
                            "description": "The explanation of the meditation and how it can be implemented."
                        }
                    },
                    "required": ["title", "content"]
                }
            }
        },
        "required": ["subconscious_mind", "personalized_affirmations", "visualizations", "meditations"]
    }
}
]
        function_call = {"name": "generate_child_subconscious_report"}
        
    if index == 6:
        sun = list(filter(lambda x:x['Name'] == "Sun" , planets))[0]
        moon = list(filter(lambda x:x['Name'] == "Moon" , planets))[0]
        content = (
            f"Create a detailed Child’s True Self report for {name} based on the Sun, Moon, and Lagnam placements in their birth chart. "
            f"Sun is placed in the {number_words[sun['pos_from_asc']]} house of {sun['sign']}, Moon is placed in the {number_words[moon['pos_from_asc']]} house of {moon['sign']}, and Lagnam is in the {asc['sign']} sign.Use {name} and {gender} pronouns all over the content."
        )

        function = [
            {
                "name": "generate_child_true_self_report",
                "description": (
                    f"Generate a detailed report explaining {name}'s True Self, Outer Personality, Emotional Needs, and Core Identity "
                    "based on their Lagnam, Moon Sign, and Sun Sign placements."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "child_personality": {
                            "type": "string",
                            "description": (
                                f"Explain {name}'s outward persona, physical attributes, and natural self-expression. "
                                "Provide insights into how the child interacts with others, based on their Rising/Ascendant/Lagnam sign. "
                                "Write in a concise and engaging paragraph."
                            )
                        },
                        "emotional_needs": {
                            "type": "string",
                            "description": (
                                f"Provide insights into {name}'s emotional self, inner feelings, instincts, and reactions. "
                                "Explain the child's emotional needs based on their Moon Sign in a short paragraph."
                            )
                        },
                        "core_identity": {
                            "type": "string",
                            "description": (
                                f"Describe {name}'s core identity, including aspirations, motivations, and sense of self. "
                                "Provide insights into how the Sun Sign shapes their inner self in a concise paragraph."
                            )
                        }
                    },
                    "required": ["child_personality", "emotional_needs", "core_identity"]
                }
            }
        ]
        
        function_call = {"name": "generate_child_true_self_report"}

        
    if index == 7:
        saturn = list(filter(lambda x:x['Name'] == "Saturn" , planets))[0]
        rahu = list(filter(lambda x:x['Name'] == "Rahu" , planets))[0]
        ketu = list(filter(lambda x:x['Name'] == "Ketu" , planets))[0]
        content = (
            f"Create a detailed Child’s Karmic Life Lesson report for {name} based on Saturn, Rahu, and Ketu placements in their birth chart. "
            f"Saturn is placed in the {number_words[saturn['pos_from_asc']]} house of {saturn['sign']}, Rahu is placed in the {number_words[rahu['pos_from_asc']]} house of {rahu['sign']}, and Ketu is placed in the {ketu['pos_from_asc']} house of {ketu['sign']}. Use {name} and {gender} pronouns all over the content."
        )

        function = [
            {
                "name": "generate_child_karmic_life_pattern_report",
                "description": f"Generate a detailed report explaining {name}'s karmic life lesson based on the placements of Saturn, Rahu, and Ketu in their birth chart, considering the house placements and their significance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "child_responsibility_discipline": {
                            "type": "string",
                            "description": f"Explain {name}'s karmic life lessons Based on Saturn and Saturn Placement in the {number_words[saturn['pos_from_asc']]} house of {saturn['sign']} Sign.Explain what {name} should avoid in life based on satrun’s karmic lessons.Write in a short paragraph."
                        },
                        "child_desire_ambition": {
                            "type": "string",
                            "description": f"Explain {name}'s karmic life lessons Based on Rahu and Rahu placement in the {number_words[rahu['pos_from_asc']]} house of {rahu['sign']} Sign.Explain what {name} should avoid in life based on Rahu's karmic lessons. Also explain {name} purpose of life based on rahu placements. Write in a short paragraph."
                        },
                        "child_spiritual_wisdom": {
                            "type": "string",
                            "description": f"“Explain {name}'s karmic life lessons Based on Ketu and Ketu Placement in the {ketu['pos_from_asc']} house of {ketu['sign']} Sign.Explain what {name} should avoid in life based on ketu’s karmic Lessons. Also explain { name} Destiny based on ketu Placements Write in a short paragraph."
                        }
                    },
                    "required": ["child_responsibility_discipline", "child_desire_ambition", "child_spiritual_wisdom"]
                }
            }
        ]

        function_call = {"name": "generate_child_karmic_life_pattern_report"}
        
        
    if index == 8:
        moon = list(filter(lambda x:x['Name'] == "Moon" , planets))[0]
        content = f"Generate a report that Provide a list of indian successful and Famous Celebrities born under a {name}'s Raasi and nakshatram. Include the following details for each Celebrities. {name} details: {moon['sign']} rasi, {moon['nakshatra']} nakshatra."
        
        function = [
            {
                "name": "generate_inspirational_celebrities_list",
                "description": f"Generate a list of indian successful and Famous Celebrities born under a {name}'s Raasi and Nakshatram.",
                "parameters": {
                    "type": "object", 
                    "properties": {
                        "celebrities": {
                            "type": "array",  
                            "items": {
                                "type": "object",
                                "description": "Details of a 5 successful and Famous Celebrities.",
                                "properties": {
                                    "name": {
                                        "type": "string",
                                        "description": "The name of the Celebritie."
                                    },
                                    "field": {
                                        "type": "string",
                                        "description": "The field of expertise of the Celebritie."
                                    },
                                    "description": {
                                        "type": "string",
                                        "description": "A brief description of the Celebritie's life path, including achievements and how their Raasi and Nakshatram traits influenced their journey."
                                    }
                                },
                                "required": ["name", "field", "description"]
                            }
                        }
                    },
                    "required": ["celebrities"] 
                }
            }
        ]


        
        function_call = {"name": "generate_inspirational_celebrities_list"}
        
    if index == 9:
        content = f"""{name}'s Planetary positions : {lagnaPrompt(planets)} {secondHouse(planets,shifted_signs,2)} {secondHouse(planets,shifted_signs,3)} {secondHouse(planets,shifted_signs,4)} {secondHouse(planets,shifted_signs,5)} {secondHouse(planets,shifted_signs,6)} {secondHouse(planets,shifted_signs,7)} {secondHouse(planets,shifted_signs,8)} {secondHouse(planets,shifted_signs,9)} {secondHouse(planets,shifted_signs,10)} {secondHouse(planets,shifted_signs,11)} {secondHouse(planets,shifted_signs,12)} Write {name} Based on the above {name}'s planetary Position and Horoscope Detail  Provide {name}'s Overall  detail Life Insights and Parenting Suggestions for Nurturing {name} with their Strength and do not give disclaimer message like i am not an astrologer Consult with professional astrologer provide only astrology Insights Contents for Parenting Suggestions use {name} and {gender} pronouns all over the content."""
        
        function = [
            {
                "name": "generate_life_insights_report",
                "description": f"Generate a {name}'s detailed report providing {name}'s overall life insights and parenting suggestions based on their planetary positions and horoscope details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions": {
                            "type": "string",
                            "description": f"Provide {name}'s Life Insights predictions based on the above planetary Position and Horoscope Detail."
                        },
                        "assessment": {
                            "type": "string",
                            "description": f"Provide {name}'s Personality Assessment based on the above planetary Position and Horoscope Detail."
                        },
                        "strength": {
                            "type": "string",
                            "description": f"Provide {name}'s Strength based on the above planetary Position and Horoscope Detail."
                        },
                        "weakness": {
                            "type": "string",
                            "description": f"Provide {name}'s Weakness based on the above planetary Position and Horoscope Detail."
                        },
                        "action" : {
                            "type": "string",
                            "description": f"Provide Parenting Action Plan for {name} based on the above planetary Position and Horoscope Detail."
                        },
                        "overall" : {
                            "type": "string",
                            "description": f"Provide {name}'s Life Insights Parenting Suggestions based on the above planetary Position and Horoscope Detail."
                        },
                        "recommendations": {
                            "type": "string",
                            "description": f"Provide Nurturing Child Parenting recommendations for {name} based on the above planetary Position and Horoscope Detail."
                        }
                    },
                    "required": ["predictions", "assessment", "strength", "weakness", "action", "overall", "recommendations"]
                }
            }
        ]
        
        function_call = {"name": "generate_life_insights_report"}

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

def healthPrompt(planets,index,name,gender):
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
                    "description": f"provide 5 Spiritual Practices including Energy Healing, Sacred Sounds, Mudras, Building Habit, Food & Diet and explain their names and how to do them with guided execution steps based on Holistic Wellness Solutions in an array",
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

def PlanetPrompt(planets,name,gender):
    content = f"""Create a Planet Position detailed report for a {name} whose {planets['Name']} Placed in {planets['pos_from_asc']} House of {planets['sign']} Sign in {planets['nakshatra']} Nakshatra {f"and the {planets['Name']} is retrograted" if planets['isRetro'] else ""} use {name} and {gender} pronouns all over the content"""
    
    function = [
        {
            'name': 'generate_child_planet_report',
            'description': f"Strategies to Enhance {planets['Name']}'s Energy for Positive Benefits: Write {planets['Name']} Placement Insights, Personalized Remedies, Daily Routine and Spiritual Practice to Strengthen the {planets['Name']}'s Energy. Explain each Daily Routine and Spiritual Practice.",
            'parameters': {
                'type': 'object',
                'properties': {
                    'remedies': {
                        'type': 'array',
                        'description': f"An array of 2 Personalized Modern Remedies techniques with Life Skills Teachings, Food & Diet, with their names and how to implement them with guided execution steps in simple, easy-to-understand English based on the {name}'s {planets['Name']} position",
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
                        'description': f"An array of 2 Daily Mindful Habits building techniques with their names and how to implement them with guided execution steps in simple, easy-to-understand English based on the {name}'s {planets['Name']} position.",
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