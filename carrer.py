from openai import OpenAI
from dotenv import load_dotenv
import os 
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

zodiac =  ["Aries","Taurus" ,"Gemini","Cancer","Leo","Virgo","Libra" ,"Scorpio" ,"Sagittarius" ,"Capricorn","Aquarius","Pisces"]

zodiac_lord = ["Mars","Venus","Mercury","Moon","Sun","Mercury","Venus","Mars","Jupiter","Saturn", "Saturn","Jupiter"]

def findCarrerPred(personal_sign,planets):
    prompt = ""
    
    ascLord = list(filter(lambda x:x['Name'] == zodiac_lord[zodiac.index(personal_sign[0])], planets))[0]
    tenLord = list(filter(lambda x:x['Name'] == zodiac_lord[zodiac.index(personal_sign[9])], planets))[0]
    sixLord = list(filter(lambda x:x['Name'] == zodiac_lord[zodiac.index(personal_sign[5])], planets))[0]
    secondLord = list(filter(lambda x:x['Name'] == zodiac_lord[zodiac.index(personal_sign[1])], planets))[0]
    
    prompt = "Provide Successful career Forecasting Insights based on Key individual and career houses and its planets Nakshatra Placements for Finding Individual Successful career"
    
    prompt += f"My Lagna is {personal_sign[0]} Lagna lord {ascLord['Name']} Placed in {ascLord['pos_from_asc']} House of {ascLord['sign']} My 10th house is {personal_sign[9]} 10 House Lord {tenLord['Name']} placed in {tenLord['pos_from_asc']} House of {tenLord['sign']} in {tenLord['nakshatra']} nakshatra and My 6th house is {personal_sign[5]} 6th house lord {sixLord['Name']} is placed in {sixLord['pos_from_asc']} House of {sixLord['sign']} in {sixLord['nakshatra']} nakshatra and My 2nd house is {personal_sign[1]} 2nd house lord {secondLord['Name']} placed in {secondLord['pos_from_asc']} House of {secondLord['sign']} in {secondLord['nakshatra']} nakshatra "
    
    
    
    prompt += """Based on the above key career 10th 6th 2  houses and its Planetary Positions , what are the most successful career Options in both  professional Work  and business opportunities that lead to high reputation, wealth, fulfilment, and a strong sense of purpose in life Combine above all in the Below JSON Format
    {
        "content" : "Explain Why Suggesting these Career  choices  in professional career and Businesses Opportunities from  Career Houses Planets Placements Analysis in 50 Words Paragraph ",
        "industry_sectors " :{
            "Based on the above planetary positions, provide Top 5 most successful industry sectors with explanations  That Give fame enhancing the individual's reputation, showcasing their unique talents, and bringing joy and deep satisfaction in the below format"
            "Work title Name": "Why you suggest in 50words"
        },
        "career_choices " :  {
            "Provide Top 5 Successful Choices for Both Professional work career Path and Business Opportunities First Provide 5 career suggestions and Roles and Designations  for professional work Career Path Second Top 5 business Opportunities with Key Talents and Unique Skills with and Consider All Career Houses and its planetary positions for provide Suggestions and its Explanations in the below format"
            "work title Name": "Why you suggest in 50words"
        },
        "justification" : "Based on Above Planet Position Which One is Highly Successful professional Career Work or Business that gives  Success Fame Health Wealth Happens",
        "partnership_compatibility" : " Based on Above Planetary Position Suggest the Priority Business or Professional Work or Both",
        "career_path": "based on above Position Provide Professional work Career path Directions that provide fame Highly Successful and Healthy Wealthy Happy Life ",
        "business_career_path": "based on above Position Provide Business Career path Directions That Provide fame leads Highly Successful and Healthy Wealthy Happy Life",
        "do": "Briefly Explain What are the Dos in order to Achieve Business explain with reference of Planetary Placements  with Planetary Placements Explanations Briefly Explain What Do are in order to Achieve Business with Planetary Placements Explanations",
        "dont" :"Briefly Explain What are the  Don'ts  in order to Achieve Professional career Path with Planetary Placements Explanations Briefly Explain What Do are the Don'ts in order to Achieve Business with Planetary Placements Explanations"
    }"""
    
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user", "content": prompt
        }
    ]
    )
    
    res = completion.choices[0].message.content
    
    res = cutString(res)
    
    res_json = json.loads(res)
    
    return res_json