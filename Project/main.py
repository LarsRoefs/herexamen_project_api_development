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


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/me", response_model=schemas.User)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User is not found")
    return db_user


#@app.post("/users/{user_id}/items/", response_model=schemas.Item)
#def create_item_for_user(
 #   user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
#):
 #   return crud.create_user_item(db=db, item=item, user_id=user_id)


#@app.get("/items/", response_model=list[schemas.Item])
#def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
 #   items = crud.get_items(db, skip=skip, limit=limit)
  #  return items


@app.post("/teams/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_team = crud.get_team_by_name(db, name=team.name)
    if db_team:
        raise HTTPException(status_code=400, detail="Team is already registered")
    return crud.create_team(db=db, team=team)


@app.get("/teams/", response_model=list[schemas.Team])
def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    teams = crud.get_teams(db, skip=skip, limit=limit)
    return teams


@app.get("/teams/{team_id}", response_model=schemas.Team)
def read_team(team_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_team = crud.get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team is not found")
    return db_team


@app.post("/drivers/", response_model=schemas.driver)
def create_driver(driver: schemas.driverCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_driver = crud.get_driver_by_name(db, name=driver.name)
    if db_driver:
        raise HTTPException(status_code=400, detail="driver is already registered")
    return crud.create_driver(db=db, driver=driver)


@app.put("/drivers/", response_model=schemas.driver)
async def update_driver(driver: schemas.driverUpdate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_driver = crud.get_driver_by_name(db, name=driver.name)zz
    if db_driver:
        raise HTTPException(status_code=400, detail="driver is already registered")
    return crud.update_driver(db, driver=driver)


@app.get("/drivers/", response_model=list[schemas.driver])
def read_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    drivers = crud.get_drivers(db, skip=skip, limit=limit)
    return drivers


@app.get("/drivers/{driver_id}", response_model=schemas.driver)
def read_driver(driver_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_driver = crud.get_driver(db, driver_id=driver_id)
    if db_driver is None:
        raise HTTPException(status_code=404, detail="driver is not found")
    return db_driver


@app.delete("/drivers/", response_model=schemas.driver)
def delete_driver(driver: schemas.driverDelete, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_driver = crud.get_driver_by_name(db, name=driver.name)
    return crud.delete_driver(db=db, driver=driver)
