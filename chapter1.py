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
  
