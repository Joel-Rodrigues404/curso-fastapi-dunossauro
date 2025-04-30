from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDBSchema(UserSchema):
    id: int


class UserPuplicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserListSchema(BaseModel):
    users: list[UserPuplicSchema]
