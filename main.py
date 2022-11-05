#from fastapi import FastAPI
from fastapi import FastAPI,  File, UploadFile

app = FastAPI()

@app.get("/") 
def hello():  
    return {"message":"Hello TutLinks.com"}
