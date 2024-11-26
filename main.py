from fastapi import FastAPI
from fastapi.params import Body 
from pydantic import BaseModel 
from typing import Optional
import random

app = FastAPI()

#1
# @app.get("/") #[setting the path '/' = home ]
# def read_root():
#     return {"Hello": "World"}

#2
# @app.get("/posts") #[setting the path '/' = home ]
# def read_root():
#     return {"Hello": "This is post"}

# @app.post("/posts")
# def create_posts():
#     return {"message": "Successfully created post"}


#3
"""
Here Body taking the content and storing it into payload

adding this in body(postman) as raw --> json
{
    "title": "My First Post",
    "content": "This is the content of the post."
}
"""
# @app.post("/posts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']} content: {payload['content']}"}




#4-------------------------------------------------------
# class post(BaseModel):
#     title : str
#     content  :str
#     publish: bool = True
#     rating: Optional[int] = None
    
# @app.post("/posts")
# def root(new_post  : post):
#     print(new_post.publish)
#     print(new_post.rating)
#     print(new_post.dict())
#     return {"data" : new_post}

"""
add postmn in body section 
{
    "title": "My First Post",
    "content": "This is the content of the post.",
    "publish" : true,
    "rating" : 4
}

"""

#5---------------------------------------------------
# Define the data structure for a post using Pydantic
class Post(BaseModel):
    title: str
    content: str
    id: int
    
my_posts = [
    {"id": 1, "title": "First Post", "content": "This is my first post!"},
    {"id": 2, "title": "Second Post", "content": "Here's some more content."},
    {"id": 3, "title": "Another Post", "content": "Yet another post to read."}
]

@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()  # Convert the incoming post object to a dictionary
    post_dict['id'] = random.randrange(0, 1000)  # Assign a random ID
    my_posts.append(post_dict)  # Append the updated dictionary
    return {"data": post_dict}  # Return all posts

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p 
        
# Extract the id from the prv post api 
@app.get("/posts/{id}")
def get_post(id : int):
    print(id)
    Post=find_post(id)
    return{"post_details" : Post}


# """
# Virtal env setting 
# python virtual environment creation 
# pythom3 -m venv name(venv)
# view--> command pallet --> select interpreter --> Enter path -->..\venv\Scripts\python.exe  [env location]
# change the interpreter
# venv\Scripts\activate.bat (Tyep it in terminal(CMD PROMPT))
# venv\Scripts\Activate.ps1(POWERSHELL PROMPT)
# if it will show you the policy error change the policy temporaru=ily
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# and 
# venv\Scripts\Activate.ps1
# It will work 

# 51.38 mins
# To run the server -->
# Uvicorn main(filename):app(app = FastAPI())
# Uvicorn main(filename):app(app = FastAPI()) --reload #to reloadthe server in every refresh afetr changes

#------
# uvicorn main:app --reload
# """