from table_model import DistanceRecord
from sqlalchemy.orm import Session
from fastapi import HTTPException
from logging_configuration import logger

def store(address1, address2, miles, km, db):
    """
    Saves a new distance record in the database.
    """
    record = DistanceRecord(
        source_address=address1,
        destination_address=address2,
        distance_in_miles=miles,
        distance_in_kilometers=km,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    
    logger.info("Stored record successfully in DB")


def fetch(db: Session):
    logger.info("Fetching all history records from DB")

    try:
        records = db.query(DistanceRecord).order_by(DistanceRecord.created_at.desc()).all()
    except Exception as e:
        logger.error(f"Database fetch failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve history")

    logger.info(f"Fetched {len(records)} records successfully")

    return [
        {
            "source_address": r.source_address,
            "destination_address": r.destination_address,
            "distance_in_miles": round(r.distance_in_miles, 2),
            "distance_in_kilometers": round(r.distance_in_kilometers, 2),
        }
        for r in records
    ]
