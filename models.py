from sqlalchemy import Column, Integer, Float
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    study_hours = Column(Float)
    attendance = Column(Float)
    previous_score = Column(Float)
    final_score = Column(Float)
