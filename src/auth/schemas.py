from pydantic import BaseModel, EmailStr, Field


class UserSchemaRegister(BaseModel):
    username: str = Field(max_length=50)
    email: EmailStr
    password: str = Field(max_length=150)


class UserSchemaLogin(BaseModel):
    email: EmailStr
    password: str = Field(max_length=150)