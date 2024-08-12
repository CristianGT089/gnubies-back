from fastapi import Depends, APIRouter, HTTPException
from app.db.schemas.schemas import FormData
from app.services.register_service import register_gnubie, get_gnubies
from app.api.dependencies.dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/submit")
async def submit_form(data: FormData, db: Session = Depends(get_db)):
    try:
        register_gnubie(db=db, data=data)
        return {"message": f"Received {data.name} with email {data.email} and code {data.code}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return get_gnubies(db=db)