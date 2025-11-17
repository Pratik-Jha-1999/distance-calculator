import os
from fastapi import  HTTPException, Header

API_PASSWORD = os.getenv("API_PASSWORD")

if not API_PASSWORD:
    raise RuntimeError("API_PASSWORD is missing in your .env file!")

# -------------------------------------------------------
# AUTHENTICATION FUNCTION
# -------------------------------------------------------
def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return True