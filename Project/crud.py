from sqlalchemy.orm import Session
import sqlalchemy.orm.query
from fastapi.security import OAuth2PasswordBearer


import models
import schemas
import auth


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#Users
#Get user by id
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

#Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

#Get list of users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

#Create User
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Drivers
#Get driver by id
def get_driver(db: Session, driver_id: int):
    return db.query(models.Driver).filter(models.Driver.id == driver_id).first()

#Get driver by name
def get_driver_by_name(db: Session, name: str):
    return db.query(models.Driver).filter(models.Driver.name == name).first()

#Get list of drivers
def get_drivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Driver).offset(skip).limit(limit).all()

#Create driver
def create_driver(db: Session, driver: schemas.DriverCreate):
    db_driver = models.Driver(name=driver.name, team=driver.team, nationality=driver.nationality, racewins=driver.racewins, worldchampionships=driver.worldchampionships)
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

#Update driver
def update_driver(db: Session, driver: schemas.DriverUpdate):
    db_driver = models.Driver(name=driver.name, team=driver.team, nationality=driver.nationality, racewins=driver.racewins, worldchampionships=driver.worldchampionships)
    db.query(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

#delete driver
def delete_driver(db: Session, name: str):
    db_driver = db.query(models.Driver).filter(models.Driver.name == name)
    db.delete(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def delete_driver(db: Session, name: str):
    db_driver = db.query(models.Driver).filter(models.Driver.name == name)
    db_driver.delete(synchronize_session=False)
    db.commit()
    return 'driver is deleted'

#Teams
#Get team by id
def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()

#Get team by name
def get_team_by_name(db: Session, name: str):
    return db.query(models.Team).filter(models.Team.name == name).first()

#Get list of teams
def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Team).offset(skip).limit(limit).all()

#Create team
def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(name=team.name, headquarters=team.headquarters, racewins=team.racewins, constructorchampionships=team.constructorchampionships)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

#Update team
def update_team(db: Session, team: schemas.TeamUpdate , team_id: int):
    db_team = db.query(models.Team).filter(models.Team.id == team_id)
    db_team.update(team.dict(), synchronize_session=False)
    db.commit()
    db.refresh(db_team)
    return db_team

#delete team
def delete_team(db: Session, name: str):
    db_team = db.query(models.Team).filter(models.Team.name == name)
    db_team.delete(synchronize_session=False)
    db.commit()
    return 'Team is deleted'