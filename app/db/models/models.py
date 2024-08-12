from sqlalchemy import Column, String, Integer, Boolean, Date, JSON, ForeignKey
from app.db.database import Base

class GnubieModel(Base):
    __tablename__ = 'gnubies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), index=True)
    phone_number = Column(String(100), index=True)
    telegram_username = Column(String(100), index=True)
    occupation = Column(String(100), index=True)
    code = Column(String(100), index=True, nullable=True)  # Hacer opcional
    non_student_occupation = Column(String(100), index=True, nullable=True)  # Hacer opcional
    motivation = Column(String(1000))
    schedule = Column(String(1000))

    