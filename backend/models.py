from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String)
    age = Column(Integer)
    gender = Column(String)
    condition = Column(String)
    medication = Column(String)
    
