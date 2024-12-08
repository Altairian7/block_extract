import datatime as _dt

import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash

import database as _database

class User(_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)
    data_created = _sql.column(_sql.DateTime, default=_dt.datetime.utcow)
    
    
class Post(_database.Base):
    __tablename__ = "posts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    post_text = _sql.Column(_sql.String, index=True)
    data_created = _sql.column(_sql.DateTime, default=_dt.datetime.utcow)
    
    owner = _orm.relationship("user", back_populates="posts")