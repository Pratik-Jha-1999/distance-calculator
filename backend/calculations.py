import geocode_API
from repository import store
from fastapi import HTTPException
from logging_configuration import logger
import math


def calculate_and_store(address1, address2, unit,db):
    valid_units = {"miles", "kilometers", "both"}
    if unit.lower() not in valid_units:
        logger.warning(f"Invalid unit received: {unit}")
        raise HTTPException(status_code=400, detail="Invalid unit. Use miles, kilometers, or both.")

    logger.info(f"Calculating distance between: '{address1}' and '{address2}'")

    data1 = geocode_API.geocode(address1)
    data2 = geocode_API.geocode(address2)

    distance = get_distance(
        float(data1["latitude"]),
        float(data1["longitude"]),
        float(data2["latitude"]),
        float(data2["longitude"])
    )

    # conversions
    km = round(distance, 2)
    miles = round(distance * 0.62, 2)

    logger.info(f"Computed distances → {miles} miles, {km} km")

    try:
        store(address1, address2, miles, km, db)
        logger.info("Stored record in database successfully")
    except Exception as e:
        logger.error(f"Database write failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Database write error")

    if unit == "miles":
        return f"{miles} mi"
    elif unit == "kilometers":
        return f"{km} km"
    else:
        return f"{miles} mi,  {km} km"




def get_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points 
    on the Earth using the Haversine formula.
    
    Parameters:
        lat1, lon1: Latitude and Longitude of point 1 (in decimal degrees)
        lat2, lon2: Latitude and Longitude of point 2 (in decimal degrees)
        
    Returns:
        Distance in kilometers
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c
    return distance

