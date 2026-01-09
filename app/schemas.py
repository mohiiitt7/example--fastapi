#from pydantic import BaseModel, EmailStr
from pydantic import BaseModel, ConfigDict , EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# =======================
# USERS
# =======================

class UserCreate(BaseModel):
    email: EmailStr # type: ignore
    password: str


class UserOut(BaseModel):
    id: int
    email: str

    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    email: EmailStr  # type: ignore
    password: str


# =======================
# POSTS
# =======================

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class PostOut(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


# =======================
# AUTH / TOKEN
# =======================

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


# =======================
# VOTES
# =======================

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  # type: ignore # 1 = vote, 0 = remove vote
