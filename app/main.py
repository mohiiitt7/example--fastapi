from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings  # ✅ use settings, don’t redefine it
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware, # type: ignore
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "FastAPI JWT Auth is working 🚀!!!!"}

# from fastapi import FastAPI, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List,Optional
# from passlib.context import CryptContext
# from . import models, schemas, utils
# from .database import engine, get_db
# from .routers import post,user, auth 
# from .config import settings

# class Settings(BaseSettings):
#     database_password: str = "localhost"
#     database_username: str = "postgres"
#     secret_key: str ="4234ui243242"

# settings = Settings()

# print(settings.database_username)

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()




# app.include_router(post.router)
# app.include_router(user.router)
# app.include_router(auth.router)

# @app.get("/")
# def root():
#     return {"message": "FastAPI is running"}


# # CREATE POST
# @app.post(
#     "/posts",
#     status_code=status.HTTP_201_CREATED,
#     response_model=schemas.Post
# )
# def create_post(
#     post: schemas.PostCreate,
#     db: Session = Depends(get_db)
# ):
#     new_post = models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post


# # GET ALL POSTS
# @app.get(
#     "/posts",
#     response_model=List[schemas.Post]
# )
# def get_posts(db: Session = Depends(get_db)):
#     return db.query(models.Post).all()


# # GET SINGLE POST
# @app.get(
#     "/posts/{id}",
#     response_model=schemas.Post
# )
# def get_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if not post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Post not found"
#         )
#     return post


# # DELETE POST
# @app.delete(
#     "/posts/{id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# def delete_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id)
#     if post.first() is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Post not found"
#         )
#     post.delete(synchronize_session=False)
#     db.commit()


# # UPDATE POST
# @app.put(
#     "/posts/{id}",
#     response_model=schemas.Post
# )
# def update_post(
#     id: int,
#     updated_post: schemas.PostCreate,
#     db: Session = Depends(get_db)
# ):
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     post = post_query.first()

#     if post is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Post not found"
#         )

#     post_query.update(updated_post.dict(), synchronize_session=False)
#     db.commit()
#     return post_query.first()


# @app.post(
#     "/users",
#     status_code=status.HTTP_201_CREATED
# )
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     #hash the password - user.password
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user

# @app.get('/users/{id}',response_model=schemas.UserOut)
# def get_user(id: int, db:Session = Depends(get_db), ):
#     user = db.query(models.User).filter(models.User.id == id).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"User with id: {id} does not exist")
    
#     return user