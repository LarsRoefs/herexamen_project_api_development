from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import crud
import models
import schemas
import auth
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )

    return {"access_token": access_token, "token_type": "bearer"}

#Users
#Post
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return crud.create_user(db=db, user=user)

#Get
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

#Get user
@app.get("/users/me", response_model=schemas.User)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user

#Get user id
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User is not found")
    return db_user

#Drivers
#Post
@app.post("/drivers/", response_model=schemas.Driver)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_driver = crud.get_driver_by_name(db, name=driver.name)
    if db_driver:
        raise HTTPException(status_code=400, detail="driver is already registered")
    return crud.create_driver(db=db, driver=driver)

#Put
@app.put("/drivers/", response_model=schemas.Driver)
async def update_driver(driver: schemas.DriverUpdate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_driver = crud.get_driver_by_name(db, name=driver.name)
    if db_driver:
        raise HTTPException(status_code=400, detail="driver is already registered")
    return crud.update_driver(db, driver=driver)

#Get
@app.get("/drivers/", response_model=list[schemas.Driver])
def read_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    drivers = crud.get_drivers(db, skip=skip, limit=limit)
    return drivers

#Get driver id
@app.get("/drivers/{driver_id}", response_model=schemas.Driver)
def read_driver(driver_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_driver = crud.get_driver(db, driver_id=driver_id)
    if db_driver is None:
        raise HTTPException(status_code=404, detail="driver is not found")
    return db_driver

#delete
@app.delete("/drivers/{name}")
def delete_driver(name: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_driver = crud.get_driver_by_name(db, name=name)
    if db_driver == None:
        raise HTTPException(status_code=404, detail="driver is not found")
    else:
        crud.delete_driver(db,name)
    return "driver is deleted"

#Teams
#Post
@app.post("/teams/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_team = crud.get_team_by_name(db, name=team.name)
    if db_team:
        raise HTTPException(status_code=400, detail="Team is already registered")
    return crud.create_team(db=db, team=team)

#Get
@app.get("/teams/", response_model=list[schemas.Team])
def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    teams = crud.get_teams(db, skip=skip, limit=limit)
    return teams

#Get team id
@app.get("/teams/{team_id}", response_model=schemas.Team)
def read_team(team_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_team = crud.get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="team is not found")
    return db_team

#delete
@app.delete("/teams/{name}")
def delete_team(name: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_team = crud.get_team_by_name(db, name=name)
    if db_team == None:
        raise HTTPException(status_code=404, detail="team is not found")
    else:
        crud.delete_team(db,name)
    return "Team is deleted"
    
#Update
@app.put("/teams/{id}", response_model=schemas.Team)
def update_team(team_id: int, team: schemas.TeamUpdate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_team = crud.get_team(db, team_id=team_id)
    db_team.first()
    if db_team == None:
        raise HTTPException(status_code=404, detail="team is not found")
    else:
        crud.update_team
    return db_team.first()
