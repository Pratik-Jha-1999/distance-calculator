from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from repository import fetch
from calculations import calculate_and_store
from logging_configuration import logger
from authentication import verify_api_key
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    )

# -------------------------------------------------------
# /distance ENDPOINT 
# -------------------------------------------------------
@app.get("/distance")
def geocode_distance(
    address1: str,
    address2: str,
    unit: str,
    db: Session = Depends(get_db),
    authorized: bool = Depends(verify_api_key)
):
    logger.info(
        f"Received /distance request | address1='{address1}' | address2='{address2}' | unit='{unit}'")
    try:
        result = calculate_and_store(address1, address2, unit, db)

        logger.info(
            f"Distance successfully calculated and stored for '{address1}' to '{address2}'")
        return {"distance": result}

    except HTTPException as e:
        logger.warning(f"/distance failed: {e.detail}")
        raise e

    except Exception as e:
        logger.exception(f"Unhandled server error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


# -------------------------------------------------------
# /history ENDPOINT 
# -------------------------------------------------------
@app.get("/history")
def get_history(
    db: Session = Depends(get_db),
    authorized: bool = Depends(verify_api_key)
):
    logger.info("Received /history request")
    try:
        result = fetch(db)
        if not result:
            return {"message": "No history found."}
        return result

    except Exception as e:
        logger.error(f"Database fetch failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")