from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    username: str = Field(max_length=50)
    email: EmailStr
    password: str = Field(max_length=150)
