from pydantic import BaseModel
from typing import Optional

class FormData(BaseModel):
    name: str
    email: str
    phone_number: str
    telegram_username: str
    occupation: str
    code: Optional[str] = None  # Hacer opcional con valor por defecto de None
    non_student_occupation: Optional[str] = None  # Hacer opcional con valor por defecto de None
    motivation: str
    schedule: str
