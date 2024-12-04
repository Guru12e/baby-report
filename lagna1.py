import swisseph as swe

def calculate_lagna(datetime_str, latitude, longitude):
    """
    Calculate the Lagna (Ascendant) degree for given input.

    Args:
        datetime_str (str): Date and time in "YYYY-MM-DD HH:MM:SS" format (IST).
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.

    Returns:
        float: The Lagna degree in the Sidereal Zodiac.
    """
    # Parse the input datetime
    from datetime import datetime
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

    # Extract date and time components
    year, month, day = datetime_obj.year, datetime_obj.month, datetime_obj.day
    hour, minute = datetime_obj.hour, datetime_obj.minute

    # Combine time into decimal hours
    hour_decimal = hour + (minute / 60.0)

    # Convert to Julian Day
    jd = swe.julday(year, month, day, hour_decimal)

    # Adjust for IST timezone (UTC+5:30)
    jd_utc = jd - (5.30 / 24.0)

    # Set Ayanamsa for Sidereal Zodiac (Lahiri)
    swe.set_sid_mode(swe.SIDM_LAHIRI)

    # Get Ascendant (Lagna) in Sidereal Zodiac
    houses = swe.houses_ex(jd_utc, latitude, longitude, b'P', flags=swe.FLG_SIDEREAL)

    # Ascendant (First value in house cusps)
    ascendant_sidereal = houses[1][0]

    return ascendant_sidereal

datetime_str = "2004-12-25 05:50:00"
latitude = 8.84570345 
longitude = 77.99381783527917

lagna_degree = calculate_lagna(datetime_str, latitude, longitude)
print(f"Lagna (Ascendant) Degree (Sidereal): {lagna_degree}")