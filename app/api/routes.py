from fastapi import APIRouter
from app.api.endpoints import register

router = APIRouter()

# Importa y registra los endpoints específicos aquí
router.include_router(register.router, prefix="/api/register", tags=["register"])