import swisseph as swe
import datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from pytz import timezone

signs = [
    ("Aries", 0, 30),
    ("Taurus", 30, 60),
    ("Gemini", 60, 90),
    ("Cancer", 90, 120),
    ("Leo", 120, 150),
    ("Virgo", 150, 180),
    ("Libra", 180, 210),
    ("Scorpio", 210, 240),
    ("Sagittarius", 240, 270),
    ("Capricorn", 270, 300),
    ("Aquarius", 300, 330),
    ("Pisces", 330, 360),
]

def get_lat_lon(location_name):
    geolocator = Nominatim(user_agent="astrology_calculator")
    try:
        location = geolocator.geocode(location_name)
        if location:
            return location.latitude, location.longitude
        else:
            raise ValueError("Location not found.")
    except GeocoderTimedOut:
        raise ConnectionError("Geocoding service timed out. Please try again.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while geocoding: {e}")
 
def get_planetary_positions(date_str, lat, lon):
    date_time_ist = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    date_time_utc = convert_to_utc(date_str)

    jd = swe.julday(date_time_utc.year, date_time_utc.month, date_time_utc.day, date_time_utc.hour + date_time_utc.minute / 60.0 + date_time_ist.second / 3600.0, swe.GREG_CAL)
    
    itc_jd = jd + 0.2083333

    planets = {
        'Sun': swe.SUN,
        'Moon': swe.MOON,
        'Mercury': swe.MERCURY,
        'Venus': swe.VENUS,
        'Mars': swe.MARS,
        'Jupiter': swe.JUPITER,
        'Saturn': swe.SATURN,
    }

    swe.set_sid_mode(swe.SIDM_LAHIRI)
    
    swe.set_topo(lon, lat, 0)

    calc_flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL  

    positions = {}
    for planet, id in planets.items():
        result, _ = swe.calc_ut(jd, id, calc_flag) 
        if result:
            lon = result[0]  
            positions[planet] = lon
        else:
            print(f"Warning: Unable to calculate position for {planet}")
  
    
    house_system = b'P'
    asc_result = swe.houses(itc_jd, lat, lon, house_system)

    ascendant_degrees = asc_result[0][0] % 360   
        
    ascendant_degrees = ascendant_degrees 
    
    if ascendant_degrees < 0 :
        ascendant_degrees += 360 
            
    rahu = swe.calc_ut(jd, swe.MEAN_NODE, swe.FLG_SIDEREAL)[0][0]
    ketu = (rahu + 180) % 360

    if rahu < 0:
        rahu += 360
    if ketu < 0:
        ketu += 360
        
    positions['Rahu'] = rahu
    positions['Ketu'] = ketu
    positions['Ascendant'] = ascendant_degrees
        
    return positions

def degree_to_sign(degree):
    zodiac_lord = {
        "Aries" : "Mars",
        "Taurus"  :"Venus",
        "Gemini" :"Mercury",
        "Cancer": "Moon",
        "Leo" : "Sun",
        "Virgo": "Mercury",
        "Libra" : "Venus",
        "Scorpio":  "Mars",
        "Sagittarius" : "Jupiter",
        "Capricorn": "Saturn",
        "Aquarius" : "Saturn",
        "Pisces": "Jupiter",
    }
    
    for sign, start, end in signs:
        if start <= degree < end:
            naksha = abs(start - degree)
            return sign,zodiac_lord[sign],naksha
    return "Unknown"

def find_planets(date_str, location):
    nakshatras = [
        ("Ashwini", 0, 13.20, "Ketu"),
        ("Bharani", 13.20, 26.40, "Venus"),
        ("Krittika", 26.40, 40.00, "Sun"),
        ("Rohini", 40.00, 53.20, "Moon"),
        ("Mrigashira", 53.20, 66.40, "Mars"),
        ("Ardra", 66.40, 80.00, "Rahu"),
        ("Punarvasu", 80.00, 93.20, "Jupiter"),
        ("Pushya", 93.20, 106.40, "Saturn"),
        ("Ashlesha", 106.40, 120.00, "Mercury"),
        ("Magha", 120.00, 133.20, "Ketu"),
        ("Purva Phalguni", 133.20, 146.40, "Venus"),
        ("Uttara Phalguni", 146.40, 160.00, "Sun"),
        ("Hasta", 160.00, 173.20, "Moon"),
        ("Chitra", 173.20, 186.40, "Mars"),
        ("Swati", 186.40, 200.00, "Rahu"),
        ("Vishakha", 200.00, 213.20, "Jupiter"),
        ("Anuradha", 213.20, 226.40, "Saturn"),
        ("Jyeshtha", 226.40, 240.00, "Mercury"),
        ("Mula", 240.00, 253.20, "Ketu"),
        ("Purva Ashadha", 253.20, 266.40, "Venus"),
        ("Uttara Ashadha", 266.40, 280.00, "Sun"),
        ("Shravana", 280.00, 293.20, "Moon"),
        ("Dhanishta", 293.20, 306.40, "Mars"),
        ("Shatabhisha", 306.40, 320.00, "Rahu"),
        ("Purva Bhadrapada", 320.00, 333.20, "Jupiter"),
        ("Uttara Bhadrapada", 333.20, 346.40, "Saturn"),
        ("Revati", 346.40, 360.00, "Mercury")
    ]

    try:
        latitude, longitude = get_lat_lon(location)
    except Exception as e:
        return

    try:
        positions = get_planetary_positions(date_str, latitude, longitude)
    except Exception as e:
        print(e)
        return
    
    planets_adjusted = []
    for planet, position in positions.items():    
        if position < 0:
            position += 360
        elif position >= 360:
            position -= 360

        sign,lord,norm = degree_to_sign(position)
        planets_adjusted.append({"Name": planet, "full_degree": position,"norm_degree":norm, "sign": sign,"zodiac_lord": lord})
                
    for planet in planets_adjusted:
        for label,start,end,lord in nakshatras:
            if start < planet["full_degree"] <= end:
                planet["nakshatra"] = label
                planet["nakshatra_lord"] = lord

    return planets_adjusted


for pl in find_planets("2004-12-25 05:50:00","Madurai, Tamil Nadu , India"):
    print(pl['Name'],pl['full_degree'],pl['sign'],pl['nakshatra'])