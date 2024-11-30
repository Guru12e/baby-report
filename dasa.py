import datetime
import math
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import ephem


start_year = 0
start_month =0

nakshatra_data = [
    {"name": "Ashwini", "start_degree": 0, "end_degree": 13.3333, "ruler": "Ketu", "dasa_years": 7},
    {"name": "Bharani", "start_degree": 13.3333, "end_degree": 26.6667, "ruler": "Venus", "dasa_years": 20},
    {"name": "Krittika", "start_degree": 26.6667, "end_degree": 40, "ruler": "Sun", "dasa_years": 6},
    {"name": "Rohini", "start_degree": 40, "end_degree": 53.3333, "ruler": "Moon", "dasa_years": 10},
    {"name": "Mrigashira", "start_degree": 53.3333, "end_degree": 66.6667, "ruler": "Mars", "dasa_years": 7},
    {"name": "Ardra", "start_degree": 66.6667, "end_degree": 80, "ruler": "Rahu", "dasa_years": 18},
    {"name": "Punarvasu", "start_degree": 80, "end_degree": 93.3333, "ruler": "Jupiter", "dasa_years": 16},
    {"name": "Pushya", "start_degree": 93.3333, "end_degree": 106.6667, "ruler": "Saturn", "dasa_years": 19},
    {"name": "Ashlesha", "start_degree": 106.6667, "end_degree": 120, "ruler": "Mercury", "dasa_years": 17},
    {"name": "Magha", "start_degree": 120, "end_degree": 133.3333, "ruler": "Ketu", "dasa_years": 7},
    {"name": "Purva Phalguni", "start_degree": 133.3333, "end_degree": 146.6667, "ruler": "Venus", "dasa_years": 20},
    {"name": "Uttara Phalguni", "start_degree": 146.6667, "end_degree": 160, "ruler": "Sun", "dasa_years": 6},
    {"name": "Hasta", "start_degree": 160, "end_degree": 173.3333, "ruler": "Moon", "dasa_years": 10},
    {"name": "Chitra", "start_degree": 173.3333, "end_degree": 186.6667, "ruler": "Mars", "dasa_years": 7},
    {"name": "Swati", "start_degree": 186.6667, "end_degree": 200, "ruler": "Rahu", "dasa_years": 18},
    {"name": "Vishakha", "start_degree": 200, "end_degree": 213.3333, "ruler": "Jupiter", "dasa_years": 16},
    {"name": "Anuradha", "start_degree": 213.3333, "end_degree": 226.6667, "ruler": "Saturn", "dasa_years": 19},
    {"name": "Jyeshtha", "start_degree": 226.6667, "end_degree": 240, "ruler": "Mercury", "dasa_years": 17},
    {"name": "Moola", "start_degree": 240, "end_degree": 253.3333, "ruler": "Ketu", "dasa_years": 7},
    {"name": "Purva Ashadha", "start_degree": 253.3333, "end_degree": 266.6667, "ruler": "Venus", "dasa_years": 20},
    {"name": "Uttara Ashadha", "start_degree": 266.6667, "end_degree": 280, "ruler": "Sun", "dasa_years": 6},
    {"name": "Shravana", "start_degree": 280, "end_degree": 293.3333, "ruler": "Moon", "dasa_years": 10},
    {"name": "Dhanishta", "start_degree": 293.3333, "end_degree": 306.6667, "ruler": "Mars", "dasa_years": 7},
    {"name": "Shatabhisha", "start_degree": 306.6667, "end_degree": 320, "ruler": "Rahu", "dasa_years": 18},
    {"name": "Purva Bhadrapada", "start_degree": 320, "end_degree": 333.3333, "ruler": "Jupiter", "dasa_years": 16},
    {"name": "Uttara Bhadrapada", "start_degree": 333.3333, "end_degree": 346.6667, "ruler": "Saturn", "dasa_years": 19},
    {"name": "Revati", "start_degree": 346.6667, "end_degree": 360, "ruler": "Mercury", "dasa_years": 17}
]

def get_lat_lon(location_name):
    """Retrieve latitude and longitude for a given location name."""
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
    
def add_year(start_year,start_month,year,month):
    start_year += year
    start_month += month
    
    if start_month >= 12:
        start_month = abs( 12 - start_month) + 1
        start_year += 1
                
    return start_year,start_month
    
def decimal_to_years(year_decimal):
    years = int(year_decimal)
    to_month = year_decimal - years
    months = int(to_month * 12)
    
    return years,months

def remaining_dasa_birth(year,completed):
    year = int(year) - completed
    
    dasa_completed_year,dasa_completed_month = decimal_to_years(year)
    
    return dasa_completed_year,dasa_completed_month
        

def calculate_dasa(date_str, planet):
    year = date_str[:4]
    for nakshatra in nakshatra_data:
        if nakshatra["start_degree"] < planet["full_degree"] <= nakshatra["end_degree"]:
            planet["nakshatra"] = nakshatra["name"]
            planet["nakshatra_lord"] = nakshatra["ruler"]
            nakshatra_span = nakshatra["end_degree"] - nakshatra["start_degree"]
            planet["dasa"] = (planet["full_degree"] - nakshatra["start_degree"]) / nakshatra_span

    fraction_covered = planet["dasa"]
    remaining_dasa = dasa_periods[planet["nakshatra_lord"]] * (1 - fraction_covered)
    completed_dasa = dasa_periods[planet["nakshatra_lord"]] - remaining_dasa
    start_year, start_month = remaining_dasa_birth(year, completed_dasa)

    bhukti_periods = {}
    dasa_reorder = reoder_remaining_dasas(planet["nakshatra_lord"])

    for dasa in dasa_reorder:
        bhukti_years = dasa_periods[planet["nakshatra_lord"]] * (dasa_periods[dasa] / 120)
        bhukti_year, bhukti_month = decimal_to_years(bhukti_years)
        end_year, end_month = add_year(start_year, start_month, bhukti_year, bhukti_month)
        
        if planet["nakshatra_lord"] not in bhukti_periods.keys():
            bhukti_periods[planet["nakshatra_lord"]] = []
            bhukti_periods[planet["nakshatra_lord"]].append({
                "bhukthi": dasa,
                "start_year": start_year,
                "end_year": end_year,
                "start_month": start_month,
                "end_month": end_month
            })
            
        else:
            bhukti_periods[planet["nakshatra_lord"]].append({
                "bhukthi": dasa,
                "start_year": start_year,
                "end_year": end_year,
                "start_month": start_month,
                "end_month": end_month
            })

        start_year, start_month = end_year, end_month

    index = dasa_order.index(planet["nakshatra_lord"])

    if index == len(dasa_order) - 1:
        index = 0

    all_dasa(bhukti_periods, dasa_order[index + 1], planet["nakshatra_lord"], start_year, start_month)

    return bhukti_periods

dasa_periods = {
    "Ketu": 7,
    "Venus": 20,
    "Sun": 6,
    "Moon": 10,
    "Mars": 7,
    "Rahu": 18,
    "Jupiter": 16,
    "Saturn": 19,
    "Mercury": 17
}

dasa_order = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]

def reoder_remaining_dasas(start_dasa):
    start_index = dasa_order.index(start_dasa)
    dasa_reorder = []
    for i in range(start_index, start_index + len(dasa_order)):
        current_dasa = dasa_order[i % len(dasa_order)]
        dasa_reorder.append(current_dasa)
    return dasa_reorder

def all_dasa(bhukti_periods,dasa,stop_dasa,start_year,start_month):
    if stop_dasa == dasa:
        return 0
    dasa_reorder = reoder_remaining_dasas(dasa)
    index = dasa_order.index(dasa)
    
    for bhukti in dasa_reorder:
        bhukti_years = dasa_periods[dasa] * (dasa_periods[bhukti] / 120)
        bhukti_year,bhukti_month = decimal_to_years(bhukti_years)
        end_year,end_month = add_year(start_year,start_month,bhukti_year,bhukti_month)
        if dasa not in bhukti_periods.keys():
            bhukti_periods[dasa] = []
            bhukti_periods[dasa].append({
                "bhukthi": bhukti,
                "start_year": start_year,
                "end_year": end_year,
                "start_month": start_month,
                "end_month": end_month
            })
            
        else:
            bhukti_periods[dasa].append({
                "bhukthi": bhukti,
                "start_year": start_year,
                "end_year": end_year,
                "start_month": start_month,
                "end_month": end_month
            })
        start_year,start_month = end_year,end_month 
        
    return all_dasa(bhukti_periods,dasa_order[0],stop_dasa,start_year,start_month) if index == len(dasa_order) - 1 else all_dasa(bhukti_periods,dasa_order[index + 1],stop_dasa,start_year,start_month)
    