import fastapi as _fastapi
import sqlalchemy.orm as _orm
import email_validator as _email_check
import passlib.hash as _hash

import database as _database
import models as _models 
import schemas as _schemas


def _create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally: 
        db.close()
        
    
async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.email == email).first()



async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    try:
        valid = _email_check.validate_email(email=user.email)
        
        email = valid.email
        
    except _email_check.EmailNotValidError:
        raise _fastapi.HTTPException(status_code=404, detail="invalid Email")
    
    
    hashed_password = _hash.bcrypt.hash(user.password)
    user_obj = _models.User(email=email, hashed_password=hashed_password)
    
    
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj
    