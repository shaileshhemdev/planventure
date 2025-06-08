from pydantic import BaseModel, EmailStr, constr

class UserRegistrationSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8) # type: ignore
