import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

app = _fastapi.FastAPI()

@app.post("/api/users")
async def create_user(
    user: _schemas.UserCreate, 
    db: _orm.Session = _fastapi.Depends(_services.get_db)
): pass