import os
from fastapi import FastAPI,  File, UploadFile

app = FastAPI()

@app.get("/") 
def hello():  
    return {"message":"Hello TutLinks.com"}

@app.post("/create_file/")
def image(image: UploadFile = File(...)):
    return {"message":"Hello TutLinks.com"}
    
