from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

def generate_date():

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return str(dt_string)

class PostSchema(BaseModel):

    UserId: int
    PostTitle: str
    PostCreateDate: str = Field(default_factory=generate_date)
    PostContent: str


class UserSchema(BaseModel):

    UserFullName: str
    UserEmail: EmailStr
    UserPassword: str

class UserLoginSchema(BaseModel):

    LoginEmail: EmailStr
    LoginPassword: str

class UpdatePostSchema(BaseModel):

    UserId: int
    PostId: int
    PostTitle: str
    PostContent: str
