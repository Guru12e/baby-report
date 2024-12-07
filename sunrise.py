from astral.sun import sun
from astral import LocationInfo
from datetime import datetime
import pytz
    

def get_sun_times(lat,lon, datestr=None):
    if datestr is None:
        date = datetime.now()
    else:
        date = datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")
    
    location = LocationInfo(latitude=lat, longitude=lon)
    observer = location.observer
    
    s = sun(observer, date=date)


    sunrise = s['sunrise'].astimezone(pytz.timezone('Asia/Kolkata')).strftime('%H:%M:%S')
    sunset = s['sunset'].astimezone(pytz.timezone('Asia/Kolkata')).strftime('%H:%M:%S')

    return sunrise, sunset


