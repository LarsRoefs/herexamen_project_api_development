from pydantic import BaseModel


#class ItemBase(BaseModel):
#    title: str
#    description: str | None = None


#class ItemCreate(ItemBase):
#    pass


#class Item(ItemBase):
#    id: int
#    owner_id: int

#    class Config:
#        orm_mode = True


class DriversBase(BaseModel):
    name: str
    teams: str

        
class DriverUpdate(SpelerBase):
    name: str
    teams: str

        
class DriverCreate(SpelerBase):
    name: str
    teams: str


class DriverDelete(SpelerBase):
    name: str
    teams: str


class Driver(DriverBase):
    id: int
    Racewinner: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    #items: list[Item] = []

    class Config:
        orm_mode = True


class TeamBase(BaseModel):
    name: str
    Worldchampion: str


class TeamCreate(TeamBase):
    name: str
    Worldchampion: str


class Team(TeamBase):
    id: int
    Racewinner: bool

    class Config:
        orm_mode = True