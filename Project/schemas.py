from pydantic import BaseModel

#Users
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

#Drivers
class DriversBase(BaseModel):
    name: str
    team: str
    nationality: str
    racewins: int
    worldchampionships: int   

class DriverCreate(DriversBase):
    pass

class DriverUpdate(DriversBase):
    pass
        
class DriverDelete(DriversBase):
    pass

class Driver(DriversBase):
    id: int

    class Config:
        orm_mode = True

#Teams
class TeamBase(BaseModel):
    name: str
    headquarters: str
    racewins: int
    constructorchampionships: int

class TeamCreate(TeamBase):
    name: str
    headquarters: str
    racewins: int
    constructorchampionships: int

class TeamUpdate(TeamBase):
    name: str
    headquarters: str
    racewins: int
    constructorchampionships: int

class TeamDelete(TeamBase):
    name: str
    headquarters: str
    racewins: int
    constructorchampionships: int

class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True