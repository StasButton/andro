import os
import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
async def read_root():
    dir = os.getcwd()
    files = os.listdir(path=dir)
    st = 'empty'
    for i in files:
        if i == 'images':
            st = 'images'      
    return {"mes":st}


@app.post("/create_file/")
async def image(image: UploadFile = File(...)):
    try:
        os.mkdir("images")
    except Exception as e:
        print(e)
    file_name = os.getcwd()+"/images/"+image.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(image.file.read())
    return {"p": os.getcwd()}
    
