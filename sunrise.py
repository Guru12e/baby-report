from astral.sun import sun
from astral import LocationInfo
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from datetime import datetime
import pytz

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
    

def get_sun_times(location, datestr=None):
    if datestr is None:
        date = datetime.now()
    else:
        date = datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")
    try:
        lat, lon = get_lat_lon(location)
    except Exception as e:
        return str(e)
    
    location = LocationInfo(latitude=lat, longitude=lon)
    observer = location.observer
    
    s = sun(observer, date=date)


    sunrise = s['sunrise'].astimezone(pytz.timezone('Asia/Kolkata')).strftime('%H:%M:%S')
    sunset = s['sunset'].astimezone(pytz.timezone('Asia/Kolkata')).strftime('%H:%M:%S')

    return sunrise, sunset

