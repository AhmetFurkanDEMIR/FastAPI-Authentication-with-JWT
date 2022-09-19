from fastapi import APIRouter, Depends
from app.models.model import PostSchema, UpdatePostSchema, UserSchema, UserLoginSchema
from app.db.user import *
from app.db.post import *
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from fastapi.responses import JSONResponse

routes = APIRouter()

@routes.get("/", tags=["hello"])
def hello():
    
    return JSONResponse(content="Hello", status_code=200)


@routes.post("/user/signup", tags=["users"])
def create_user(user: UserSchema):
    
    flag = createUser(user.UserFullName, user.UserEmail, user.UserPassword)


    if flag==0:
        return JSONResponse(content="Error!", status_code=500)

    else:

        return JSONResponse(content="Add user successful", status_code=201)

@routes.post("/user/login", tags=["users"])
def user_login(user: UserLoginSchema):

    if checkUser(user.LoginEmail, user.LoginPassword):
        return signJWT(user.LoginEmail)
    return JSONResponse(content="Wrong login details!", status_code=500)


@routes.post("/post/", dependencies=[Depends(JWTBearer())], tags=["posts"])
def add_post(post: PostSchema):

    flag = addPost(post.UserId, post.PostTitle, post.PostCreateDate, post.PostContent)
    
    if flag==0:

        return JSONResponse(content="Error", status_code=500)

    else:

        return JSONResponse(content="Post Added", status_code=201)

@routes.get("/post/", dependencies=[Depends(JWTBearer())], tags=["posts"])
def get_all_posts():

    posts = getAllPost()

    if posts==0:

        return JSONResponse(content="Error", status_code=500)
    else:

        return JSONResponse(content=posts, status_code=200)

@routes.get("/post/{id}", dependencies=[Depends(JWTBearer())], tags=["posts"])
def get_id_post(id: int):
    
    post = getIdPost(id)

    if post == -99:

        return JSONResponse(content="Error", status_code=500)

    else:

        return JSONResponse(content=post, status_code=200)


@routes.delete("/post/{id}", dependencies=[Depends(JWTBearer())], tags=["posts"])
def delete_id_post(id: int):
    
    post = deleteIdPost(id)

    if post == 0:

        return JSONResponse(content="Error", status_code=500)

    else:

        return JSONResponse(content="Post deletion successful", status_code=200)


@routes.put("/post/", dependencies=[Depends(JWTBearer())], tags=["posts"])
def update_post(post: UpdatePostSchema):
    
    post = updatePost(post.UserId, post.PostId, post.PostTitle, post.PostContent)

    if post == 0:

        return JSONResponse(content="Error", status_code=500)

    else:

        return JSONResponse(content="Post update successful", status_code=200)