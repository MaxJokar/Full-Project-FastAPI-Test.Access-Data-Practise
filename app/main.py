from fastapi import FastAPI
from blog.database import engine
from blog.routers import blog, user, authentication
from blog import models

# from passlib.context import CryptContext


app = FastAPI()
# create all the models into DB
# (table or migrate all tables  in our   database table)
models.Base.metadata.create_all(engine)

#  desplay separately on Swagger UI
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
