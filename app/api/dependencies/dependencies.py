from app.db.database import engine, localSession, Base

Base.metadata.create_all(bind=engine)

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()
