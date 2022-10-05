import os
os.chdir('C:\Stas2\Python_projecs') 

from fastapi import FastAPI


app = FastAPI()
@app.get("/")
async def root():
    
    return {"message": "Hello World"}

