from fastapi import FastAPI, HTTPException
from logging_configuration import logger
import requests

app = FastAPI(
    title="Nominatim Geocoding API",
    description="Backend to perform geocoding and reverse geocoding using OpenStreetMap Nominatim API.",
    version="1.0.0"
)

USER_AGENT = "MyApp/1.0 (pratikgns@gmail.com)"  
def geocode(address: str):
    if not address or address.strip() == "":
        logger.warning(f"Empty address received: '{address}'")
        raise HTTPException(status_code=400, detail="Address cannot be empty.")

    logger.info(f"Geocoding address: {address}")

    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json", "limit": 1}
    headers = {"User-Agent": USER_AGENT}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.Timeout:
        logger.error(f"Timeout while calling Nominatim API for: {address}")
        raise HTTPException(status_code=504, detail="Geocoding API request timed out.")
    except requests.ConnectionError:
        logger.error("Connection error while reaching Nominatim API.")
        raise HTTPException(status_code=503, detail="Failed to connect to geocoding API.")
    except requests.RequestException as e:
        logger.error(f"Nominatim API request failed: {str(e)}")
        raise HTTPException(status_code=502, detail=f"API error: {str(e)}")

    if not data:
        logger.warning(f"No geocoding results found for: {address}")
        raise HTTPException(status_code=404, detail=f"No results found for address '{address}'")

    logger.info(f"Geocoding successful for: {address}")

    return {
        "latitude": data[0]["lat"],
        "longitude": data[0]["lon"],
        "display_name": data[0]["display_name"]
    }
