from fastapi import FastAPI

app = FastAPI()


@app.get("/") #[setting the path '/' = home ]
def read_root():
    return {"Hello": "World"}


@app.get("/post") #[setting the path '/' = home ]
def read_root():
    return {"Hello": "This is post"}
"""
51.38 mins
To run the server -->
Uvicorn main(filename):app(app = FastAPI())
Uvicorn main(filename):app(app = FastAPI()) --reload #to reloadthe server in every refresh afetr changes
"""