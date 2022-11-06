import os
import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
async def read_root():
    dir = os.getcwd()+'/folder/'
    files = os.listdir(path=dir)        
    return {"mes":files}


@app.post("/upload_file/")
async def image(image: UploadFile = File(...)):
    '''
    try:
        os.mkdir("images")
    except Exception as e:
        print(e)
    '''
    file_name = os.getcwd()+"/folder/"+image.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(image.file.read())
    return {"p": os.getcwd()}


from fastapi.responses import FileResponse
#from os import getcwd, remove

@app.get("/dl/{name_file}")
def download_file(name_file: str):
    return  FileResponse(path=os.getcwd() + "/folder/" + name_file, media_type='application/octet-stream', filename=name_file)

@app.get("/del/")  
def dF():
    dir = os.getcwd()+'/folder/'
    files = os.listdir(path=dir)

    for i in files:
        try:
            os.remove(dir + i)
        except FileNotFoundError:
            return 'remove fail'
    
    
    return files

@app.post("/create_folder/")
async def fold():
    try:
        os.mkdir("folder")
    except Exception as e:
        print(e)
