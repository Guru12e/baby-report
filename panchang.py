import datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from sunrise import get_sun_times
import ephem
import math
import time

ganam_nakshatras = {
    "Deva_Ganam": [
        "Ashwini",
        "Mrigashira",
        "Punarvasu",
        "Pushya",
        "Hasta",
        "Swati",
        "Anuradha",
        "Shravana",
        "Revati"
    ],
    "Manushya_Ganam": [
        "Bharani",
        "Rohini",
        "Ardra",
        "Purva Phalguni",
        "Uttara Phalguni",
        "Purva Ashadha",
        "Uttara Ashadha",
        "Purva Bhadrapada",
        "Uttara Bhadrapada"
    ],
    "Rakshasa_Ganam": [
        "Krittika",
        "Ashlesha",
        "Magha",
        "Chitra",
        "Vishakha",
        "Jyeshtha",
        "Mula",
        "Dhanishta",
        "Shatabhisha"
    ]
}

nakshatra_yoni = {
    'Ashwini': 'Horse',
    'Bharani': 'Elephant',
    'Krittika': 'Sheep',
    'Rohini': 'Snake',
    'Mrigashira': 'Snake', 
    'Ardra': 'Dog',
    'Punarvasu': 'Cat', 
    'Pushya': 'Sheep',
    'Ashlesha': 'Cat', 
    'Magha': 'Rat', 
    'Purva Phalguni': 'Rat',
    'Uttara Phalguni': 'Cow',
    'Hasta': 'Buffalo', 
    'Chitra': 'Tiger',
    'Swati': 'Buffalo', 
    'Vishakha': 'Tiger',
    'Anuradha': 'Deer', 
    'Jyeshtha': 'Deer', 
    'Mula': 'Dog',
    'Purva Ashadha': 'Monkey',
    'Uttara Ashadha': 'Mongoose',
    'Shravana': 'Monkey', 
    'Dhanishta': 'Lion', 
    'Shatabhisha': 'Horse', 
    'Purva Bhadrapada': 'Lion', 
    'Uttara Bhadrapada': 'Cow', 
    'Revati': 'Elephant'
}

def get_lat_lon(location_name, max_retries=3, timeout_duration=5):
    """Retrieve latitude and longitude for a given location name."""
    geolocator = Nominatim(user_agent="astrology_calculator")

    for attempt in range(max_retries):
        try:
            location = geolocator.geocode(location_name, timeout=timeout_duration)
            if location:
                return location.latitude, location.longitude
            else:
                raise ValueError("Location not found.")
        except GeocoderTimedOut:
            print(f"Attempt {attempt + 1} timed out. Retrying...")
            time.sleep(2)  
        except Exception as e:
            raise RuntimeError(f"An error occurred while geocoding: {e}")
    
    raise ConnectionError("Failed to retrieve location after multiple attempts.")

nakshatrasData = [
    (0.000000000000000, 13.333333333333334),   
    (13.333333333333334, 26.666666666666668),  
    (26.666666666666668, 40.000000000000000),  
    (40.000000000000000, 53.333333333333336),  
    (53.333333333333336, 66.666666666666671),  
    (66.666666666666671, 80.000000000000014),  
    (80.000000000000014, 93.333333333333343),  
    (93.333333333333343, 106.666666666666686), 
    (106.666666666666686, 120.000000000000030),
    (120.000000000000030, 133.333333333333370),
    (133.333333333333370, 146.666666666666710),
    (146.666666666666710, 160.000000000000060),
    (160.000000000000060, 173.333333333333400),
    (173.333333333333400, 186.666666666666740),
    (186.666666666666740, 200.000000000000090),
    (200.000000000000090, 213.333333333333430),
    (213.333333333333430, 226.666666666666770),
    (226.666666666666770, 240.000000000000110),
    (240.000000000000110, 253.333333333333450),
    (253.333333333333450, 266.666666666666790),
    (266.666666666666790, 280.000000000000140),
    (280.000000000000140, 293.333333333333480),
    (293.333333333333480, 306.666666666666820),
    (306.666666666666820, 320.000000000000170),
    (320.000000000000170, 333.333333333333510),
    (333.333333333333510, 346.666666666666850),
    (346.666666666666850, 360.000000000000200) 
]


def calculate_tithi(sun_pos, moon_pos):
    tithis = ["Pratipada", "Ditiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima"]
    sun_longitude, moon_longitude =sun_pos,moon_pos
    difference = moon_longitude - sun_longitude
    if difference < 0:
        difference += 360

    tithi = math.ceil(difference / 12)
    paksha = "Shukla Paksha" if tithi <= 15 else "Krishna Paksha"
    
    if tithi == 30:
        return "Amavasya",30,"Krishna Paksha"

    return tithis[(tithi % 15)- 1],tithi,paksha


def calculate_nakshatra(moon_pos):
    nakshatra_degrees = moon_pos 
    nakshatras = ["Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"]
    nakshatra_index = int(nakshatra_degrees / 13.333333333333334) % 27
            
    return nakshatras[nakshatra_index],nakshatra_index

def calculate_yoga(moon_pos, sun_pos):
    angular_diff = (sun_pos + moon_pos) / 13.33333333333
    if angular_diff < 0:
        angular_diff += 360
    
    yoga_index = int(angular_diff) % 27
    yogas = [
        "Vishkambha",
        "Priti",
        "Ayushman",
        "Saubhagya",
        "Shobhana",
        "Atiganda",
        "Sukarman",
        "Dhriti",
        "Shoola",
        "Ganda",
        "Vriddhi",
        "Dhruva",
        "Vyaghata",
        "Harsana",
        "Vajra",
        "Siddhi",
        "Vyatipata",
        "Variyana",
        "Parigha",
        "Shiva",
        "Siddha",
        "Sadhya",
        "Shubha",
        "Shukla",
        "Brahma",
        "Indra",
        "Vaidhriti"
    ]
    
    return yogas[yoga_index], yoga_index

def calculate_karana(tithi,sun_pos, moon_pos):
    karanas = [
        ["Kinstughna", 	"Bava" ],
     	["Balava" 	,"Kaulava" ],
     	["Taitila" 	,"Garaja" ],
    	["Vanija" 	,"Vishti" ],
     	["Bava" 	,"Balava" ],
     	["Kaulava" 	,"Taitila" ],
     	["Garaja" 	,"Vanija" ],
     	["Vishti" 	,"Bava" ],
     	["Balava" 	,"Kaulava" ],
        ["Taitila" 	,"Garaja" ],
        ["Vanija" 	,"Vishti" ],
        ["Bava" 	,"Balava" ],
        ["Kaulava" 	,"Taitila" ],
        ["Garaja" 	,"Vanija" ],
        ["Vishti" 	,"Shakuni" ],
        ["Balava" 	,"Kaulava" ],
        ["Taitila" 	,"Garaja" ],
        ["Vanija" 	,"Vishti" ],
        ["Bava" 	,"Balava" ],
        ["Kaulava" 	,"Taitila" ],
        ["Garaja" 	,"Vanija" ],
        ["Vishti" 	,"Bava" ],
        ["Balava" 	,"Kaulava" ],
        ["Taitila" 	,"Garaja" ],
        ["Vanija" 	,"Vishti" ],
        ["Bava" 	,"Balava" ],
        ["Kaulava" 	,"Taitila" ],
        ["Garaja" 	,"Vanija" ],
        ["Vishti" 	,"Shakuni" ],
        ["Chatushpada" 	,"Nagava"]
    ]
     
    sun_longitude, moon_longitude =sun_pos,moon_pos
    difference = moon_longitude - sun_longitude
    if difference < 0:
        difference += 360
        
    value = difference / 12
    
    rounded_value = round(value, 2)

    decimal_part = (rounded_value * 100) % 100
    
    if decimal_part > 50:
        return karanas[tithi - 1][1] , tithi * 2 
    else:
        return karanas[tithi - 1][0] , (tithi * 2 ) - 1
    
    
def calculate_panchang(date_str, moon_pos, sun_pos, location):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    day_of_week = date_obj.strftime('%A')
        
    thithi,thithi_number,paksha = calculate_tithi(sun_pos,moon_pos)
    nakshatra,nakshatraIndex = calculate_nakshatra(moon_pos)
    yoga,yoga_index = calculate_yoga(sun_pos,moon_pos)
    karanam,karanamIndex = calculate_karana(thithi_number,sun_pos,moon_pos)
    sunrise,sunset = get_sun_times(location,date_str)
    
    panchang_values = {
        "thithi": thithi,
        "thithi_number": thithi_number,
        "nakshatra" : nakshatra, 
        "nakshatra_number" : nakshatraIndex + 1,
        "yoga": yoga,
        "yoga_index": yoga_index,
        "karanam": karanam,
        "karanam_number" : karanamIndex,
        "paksha": paksha,
        "week_day": day_of_week,
        "sunrise": sunrise,
        "sunset": sunset,
        "ganam" : "Deva" if nakshatra in ganam_nakshatras["Deva_Ganam"] else "Manushya" if nakshatra in ganam_nakshatras["Manushya_Ganam"] else "Rakshasa",
        "yoni" : nakshatra_yoni[nakshatra]
    }
    
    return panchang_values

