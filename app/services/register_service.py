from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.db.schemas.schemas import FormData
from app.db.models.models import GnubieModel

def register_gnubie(db: Session, data: FormData):
    # Verificar si el correo ya existe en la base de datos
    existing_gnubie = db.query(GnubieModel).filter(GnubieModel.email == data.email).first()
    
    if existing_gnubie:
        # Si ya existe un usuario con el mismo correo, devolver un error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este correo ya está registrado."
        )

    # Si no existe, crear el nuevo gnubie
    new_gnubie = GnubieModel(
        name=data.name, 
        email=data.email, 
        phone_number=data.phone_number,
        telegram_username=data.telegram_username,
        occupation=data.occupation,
        code=data.code,  # Puede ser None
        non_student_occupation=data.non_student_occupation,  # Puede ser None
        motivation=data.motivation,
        schedule=data.schedule
    )
    
    db.add(new_gnubie)
    db.commit()
    db.refresh(new_gnubie)

    return new_gnubie

def get_gnubies(db: Session):
    return db.query(GnubieModel).all()