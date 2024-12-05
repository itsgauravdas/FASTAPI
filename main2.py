import psycopg2 
from psycopg2.extras import RealDictCursor
import time
from fastapi import FastAPI,status
from pydantic import BaseModel 
from fastapi import FastAPI,Response,status,HTTPException

app=FastAPI()
class post(BaseModel):
    title : str
    content  :str
    published : bool =True
    
    

while True: 
    try:
        conn=psycopg2.connect(host= 'localhost',database='fastapi',
                            user = 'postgres', password ='12345', cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as e:
        print("Connection DataBase failed")
        print("error :", e)
        time.sleep(2)
 

#Select
#To get the data from postgres
@app.post("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts=cursor.fetchall()
    print(posts)
    return {"data"  : posts}

#Insert
@app.post("/post/ins", status_code=status.HTTP_201_CREATED)
def create_post(post: post):
    cursor.execute(""" insert into posts (title,content, published) values (%s, %s, %s) RETURNING * """,
                            (post.title,post.content,post.published))
    new_post=cursor.fetchone()
    conn.commit()
    return {"data": new_post}

    
#Where


@app.get("/postss/{id}")
def get_post(id : int):
    cursor.execute("""SELECT * FROM posts where id = %s """, (str(id)))
    test_post=cursor.fetchone()
    print(test_post)
    if not test_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id: {id} was not found")
    return {"post" : test_post}

#Delete
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def del_post(id : int):
    cursor.execute(""" DELETE FROM posts where id = %s RETURNING * """, (str(id),))
    del_post=cursor.fetchone()
    conn.commit()
    if del_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id: {id} was not found")
    return {"post" : del_post}
        
    