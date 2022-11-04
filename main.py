import os
import uvicorn
from fastapi import FastAPI,  File, UploadFile
#from fastapi.routing import APIRoute,APIRouter
#from fastapi.encoders import jsonable_encoder
#import shutil

app = FastAPI()

@app.get("/")
async def read_root():
    return "Hello Stas Fe"

@app.post("/create_file/")
async def image(image: UploadFile = File(...)):
    try:
        os.mkdir("images")
    except Exception as e:
        print(e)
    file_name = os.getcwd()+"/images/"+image.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(image.file.read())
        #f.close()
    #file = jsonable_encoder({"imagePath":file_name})
    #new_image = await add_image(file)
    #return {"filename": new_image}
    return {"filename": file_name}



