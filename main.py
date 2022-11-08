import os
#import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

import numpy as np
app = FastAPI()


@app.get("/")
async def read_root():
    #dir = os.getcwd() +'/streamlit/'
    #files = os.listdir(path=dir) 
    #d = np.array([1,2,3])
    return 'OK'

'''
@app.post("/upload_file/")
async def image(image: UploadFile = File(...)):
    #file_name = os.getcwd()+"/folder/"+image.filename.replace(" ", "-")
    file_name = os.getcwd()+"/fold/"+image.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(image.file.read())
    return {"p": os.getcwd()}


@app.get("/dl/{name_file}")
def download_file(name_file: str):
    #return  FileResponse(path=os.getcwd() + "/folder/" + name_file, media_type='application/octet-stream', filename=name_file)
    return  FileResponse(path=os.getcwd() + "/fold/" + name_file, media_type='application/octet-stream', filename=name_file)

@app.get("/del/")  
def dF():
    dir = os.getcwd() +'/fold/'
    files = os.listdir(path=dir)
    
    for i in files:
        try:
            os.remove(dir + i)
        except FileNotFoundError:
            return 'remove fail'
    return files

@app.get("/cl/")
async def fold():
    dir = os.getcwd() +'/fold/'
    files = os.listdir(path=dir)
    for i in files:
        try:
            os.remove(dir + i)
        except FileNotFoundError:
            return 'remove fail'
    return 'all OK'
'''
