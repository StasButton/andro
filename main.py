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


'''

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)





#@app.post("/uploadfiles")
async def create_upload_file(file: UploadFile = File(...)):
    res = await file.read()# Read file content
    with open(file.filename, "wb") as f:# Write the file by file name
            f.write(res)
    return {"message": "success"}


routes = [
    APIRoute(path="/", endpoint=read_root, methods=["GET"]),
    APIRoute(path="/uploadfiles", endpoint=create_upload_file, methods=["POST"])
    ]
    
app = FastAPI()
app.include_router(APIRouter(routes=routes))

import uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=80)


@app.post("/upload-file")
async def create_upload_file(file: UploadFile = File(...)):
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer )
        #shutil.copyfileobj(fileh.file, buffer )
        fileh = file
    return {"filename = ": file.filename} # getting filename


import shutil

@app.get("/{value}")
async def read_item(value: int):
    sqr = value**2
    return  sqr

@app.get("/{value}")
async def read_item(value: int):
    sqr = value**2
    return  sqr

#=========================================


'''



