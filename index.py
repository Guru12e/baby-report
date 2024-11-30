import swisseph as swe
import datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

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

    date_time_utc = date_time_ist - datetime.timedelta(hours=5, minutes=30)

    jd = swe.julday(date_time_utc.year, date_time_utc.month, date_time_utc.day, date_time_utc.hour + date_time_utc.minute / 60.0 + date_time_ist.second / 3600.0, swe.GREG_CAL)

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
    asc_result = swe.houses(jd, lat, lon, house_system)

    ascendant_degrees = asc_result[0][0] % 360   
        
    ascendant_degrees = ascendant_degrees - 21.13829813984028
    
    if ascendant_degrees < 0 :
        ascendant_degrees += 360 
        
    positions['Ascendant'] = ascendant_degrees
    
    TRUE_NODE = swe.TRUE_NODE

    rahu_result = swe.calc_ut(jd, TRUE_NODE)
    rahu_longitude = rahu_result[0][0] 

    ketu_longitude = ((rahu_longitude + 180) % 360) - 23.415156475773582

    rahu_longitude = rahu_longitude - 23.415156475773568

    if rahu_longitude < 0:
        rahu_longitude += 360
    if ketu_longitude < 0:
        ketu_longitude += 360
        
    positions['Rahu'] = rahu_longitude
    positions['Ketu'] = ketu_longitude
        
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
    padasList = {
    "Ashwini": [
        [1, 0, 3.20],
        [2, 3.20, 6.40],
        [3, 6.40, 10],
        [4, 10, 13.20]
    ],
    "Bharani": [
        [1, 13.20, 16.40],
        [2, 16.40, 20],
        [3, 20, 23.20],
        [4, 23.20, 26.40]
    ],
    "Krittika": [
        [1, 26.40, 30],
        [2, 30, 33.20],
        [3, 33.20, 36.40],
        [4, 36.40, 40]
    ],
    "Rohini": [
        [1, 40, 43.20],
        [2, 43.20, 46.40],
        [3, 46.40, 50],
        [4, 50, 53.20]
    ],
    "Mrigashira": [
        [1, 53.20, 56.40],
        [2, 56.40, 60],
        [3, 60, 63.20],
        [4, 63.20, 66.40]
    ],
    "Ardra": [
        [1, 66.40, 70],
        [2, 70, 73.20],
        [3, 73.20, 76.40],
        [4, 76.40, 80]
    ],
    "Punarvasu": [
        [1, 80, 83.20],
        [2, 83.20, 86.40],
        [3, 86.40, 90],
        [4, 90, 93.20]
    ],
    "Pushya": [
        [1, 93.20, 96.40],
        [2, 96.40, 100],
        [3, 100, 103.20],
        [4, 103.20, 106.40]
    ],
    "Ashlesha": [
        [1, 106.40, 110],
        [2, 110, 113.20],
        [3, 113.20, 116.40],
        [4, 116.40, 120]
    ],
    "Magha": [
        [1, 120, 123.20],
        [2, 123.20, 126.40],
        [3, 126.40, 130],
        [4, 130, 133.20]
    ],
    "Purva Phalguni": [
        [1, 133.20, 136.40],
        [2, 136.40, 140],
        [3, 140, 143.20],
        [4, 143.20, 146.40]
    ],
    "Uttara Phalguni": [
        [1, 146.40, 150],
        [2, 150, 153.20],
        [3, 153.20, 156.40],
        [4, 156.40, 160]
    ],
    "Hasta": [
        [1, 160, 163.20],
        [2, 163.20, 166.40],
        [3, 166.40, 170],
        [4, 170, 173.20]
    ],
    "Chitra": [
        [1, 173.20, 176.40],
        [2, 176.40, 180],
        [3, 180, 183.20],
        [4, 183.20, 186.40]
    ],
    "Swati": [
        [1, 186.40, 190],
        [2, 190, 193.20],
        [3, 193.20, 196.40],
        [4, 196.40, 200]
    ],
    "Vishakha": [
        [1, 200, 203.20],
        [2, 203.20, 206.40],
        [3, 206.40, 210],
        [4, 210, 213.20]
    ],
    "Anuradha": [
        [1, 213.20, 216.40],
        [2, 216.40, 220],
        [3, 220, 223.20],
        [4, 223.20, 226.40]
    ],
    "Jyeshtha": [
        [1, 226.40, 230],
        [2, 230, 233.20],
        [3, 233.20, 236.40],
        [4, 236.40, 240]
    ],
    "Mula": [
        [1, 240, 243.20],
        [2, 243.20, 246.40],
        [3, 246.40, 250],
        [4, 250, 253.20]
    ],
    "Purva Ashadha": [
        [1, 253.20, 256.40],
        [2, 256.40, 260],
        [3, 260, 263.20],
        [4, 263.20, 266.40]
    ],
    "Uttara Ashadha": [
        [1, 266.40, 270],
        [2, 270, 273.20],
        [3, 273.20, 276.40],
        [4, 276.40, 280]
    ],
    "Shravana": [
        [1, 280, 283.20],
        [2, 283.20, 286.40],
        [3, 286.40, 290],
        [4, 290, 293.20]
    ],
    "Dhanishta": [
        [1, 293.20, 296.40],
        [2, 296.40, 300],
        [3, 300, 303.20],
        [4, 303.20, 306.40]
    ],
    "Shatabhisha": [
        [1, 306.40, 310],
        [2, 310, 313.20],
        [3, 313.20, 316.40],
        [4, 316.40, 320]
    ],
    "Purva Bhadrapada": [
        [1, 320, 323.20],
        [2, 323.20, 326.40],
        [3, 326.40, 330],
        [4, 330, 333.20]
    ],
    "Uttara Bhadrapada": [
        [1, 333.20, 336.40],
        [2, 336.40, 340],
        [3, 340, 343.20],
        [4, 343.20, 346.40]
    ],
    "Revati": [
        [1, 346.40, 350],
        [2, 350, 353.20],
        [3, 353.20, 356.40],
        [4, 356.40, 360]
    ]
}

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
        return
    
    planets_adjusted = []
    for planet, position in positions.items():    
        if position < 0:
            position += 360
        elif position >= 360:
            position -= 360

        sign,lord,norm = degree_to_sign(position)
        planets_adjusted.append({"Name": planet, "full_degree": position,"norm_degree":norm, "sign": sign,"zodiac_lord": lord})
            
    orderPlanet = sorted(planets_adjusted,key=lambda k: k["norm_degree"],reverse=True)
    startRasi = list(filter(lambda x: x["Name"] == "Ascendant",planets_adjusted))[0]["sign"]
    signsOrder = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
    signOrderFromAsc = signsOrder[signsOrder.index(startRasi):] + signsOrder[:signsOrder.index(startRasi)]
    
    for planet in planets_adjusted:
        for label,start,end,lord in nakshatras:
            if start < planet["full_degree"] <= end:
                planet["nakshatra"] = label
                planet["nakshatra_lord"] = lord
                for pada,start,stop in padasList[label]:
                    if start <= planet["full_degree"] <= stop:
                        planet["pada"] = pada
                        planet["order"] = orderPlanet.index(planet) + 1
                        planet["pos_from_asc"] = (signOrderFromAsc.index(planet["sign"]) + 1)

    return planets_adjusted
