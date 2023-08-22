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
    teams: str

        
class DriverUpdate(DriversBase):
    name: str
    teams: str
    Racewinner: bool

        
class DriverCreate(DriversBase):
    name: str
    teams: str
    Racewinner: bool


class DriverDelete(DriversBase):
    name: str
    teams: str
    Racewinner: bool


class Driver(DriversBase):
    id: int
    Racewinner: bool

    class Config:
        orm_mode = True

#Teams
class TeamBase(BaseModel):
    name: str
    Contructorchampion: bool


class TeamCreate(TeamBase):
    name: str
    Contructorchampion: bool


class Team(TeamBase):
    id: int
    Contructorchampion: bool

    class Config:
        orm_mode = True