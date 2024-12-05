from fastapi import FastAPI, Response,status
from fastapi.params import Body 
from pydantic import BaseModel 
from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
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
# class Post(BaseModel):
#     title: str
#     content: str
#     # id: int
#     rating: Optional[int] = None
    
    
    
my_posts = [
    {"id": 1, "title": "First Post", "content": "This is my first post!"},
    {"id": 2, "title": "Second Post", "content": "Here's some more content."},
    {"id": 3, "title": "Another Post", "content": "Yet another post to read."}
]

# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_post(post: Post):
#     post_dict = post.dict()  # Convert the incoming post object to a dictionary
#     post_dict['id'] = random.randrange(0, 1000)  # Assign a random ID
#     my_posts.append(post_dict)  # Append the updated dictionary
#     return {"data": post_dict}  # Return all posts

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p 
        
# Extract the id from the prv post api 
# @app.get("/posts/{id}")
# def get_post(id : int, response: Response):
#     print(id)
#     Post=find_post(id)
#     if not Post:
#         # response.status_code = 404
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'message' : f"post with {id} was not found"}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with {id} was not found")
#     return{"post_details" : Post}

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}

#------Delete ------Start
# def find_index_post(id : int):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i
#     return None
        
# @app.delete("/posts/{id}", status_code=status.HTTP_200_OK)
# def delete_post(id: int):
#     index = find_index_post(id)
#     if index is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     my_posts.pop(index)
#     return {"message": "Post was successfully deleted"}
#------END

#---update(PUT)


# def find_index_post(id : int):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i
#     return None


# @app.put("/posts/{id}")
# def update_post(id : int, post: Post, response: Response):
#     print(post)
#     index = find_index_post(id)
#     if index is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     post_dict=post.dict()
#     post_dict['id'] = id
#     my_posts[index] = post_dict
    
#     return {'data' : post_dict}
    

# @app.get("/posts/{id}")
# def get_posts(id: int, response : Response):
#     post=find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id}")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'message' : f"post with id: {id}"}
#     return {"post_details" : post}
    
    
    


#---END



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