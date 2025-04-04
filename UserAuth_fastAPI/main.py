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
): 
    db_user = await _services.get_user_by_email(email=user.email, db=db)
    if db_user:
        raise _fastapi.HTTPException(
            status_code=400, detail="Already exists"
        )
        
        
    # create user
    user = await _services.create_user(user=user, db=db)
    
    # return the token 
    return await _services.create_token(user=user)


@app.post("/api/token")
async def generate_token(
    form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(),
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    user = await _services.authenticate_user(email=form_data.username, password=form_data.password, db=db)
    
    if not user:
        raise _fastapi.HTTPException(status_code=401, detail="Invalid")
    
    return await _services.create_token(user=user)


@app.get("/api/users/me", response_model=_schemas.User)
async def get_user(user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
    return user

@app.post("/api/posts", response_model=_schemas.Post)
async def create_post(post: _schemas.PostCreate, 
                      user: _schemas.User = _fastapi.Depends(_services.get_current_user), 
                      db: _orm.Session = _fastapi.Depends(_services.get_db),
                      ): 
    return await _services.create_post(user=user, db=db, post=post)