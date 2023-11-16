from fastapi import FastAPI, status, Depends, HTTPException
import Models
from Database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
import Auth
from Auth import get_current_user

app = FastAPI()
app.include_router(Auth.router)

Models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"user": user}