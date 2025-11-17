from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, text
from database import Base

class DistanceRecord(Base):
    __tablename__ = "distance_records"

    id = Column(Integer, primary_key=True, index=True)
    source_address = Column(String, nullable=False)
    destination_address = Column(String, nullable=False)
    distance_in_miles = Column(Float, nullable=False)
    distance_in_kilometers = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
