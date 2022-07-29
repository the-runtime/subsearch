from fastapi import FastAPI, File, UploadFile
from starlette.background import BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import aiofiles

import query
from process_video import process_vid
import get_database

#container = get_database.get_container()

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile, background_tasks: BackgroundTasks):
    try :
        filename = file.filename
        #contents = await file.read()

        async with aiofiles.open(filename,'wb') as f:
            i=0
            size = 1024*50
            while content := await file.read(size):
                await f.write(content)
                i = i+1
                print(f"{i} bytes  written")
        f.close()
    except Exception:
        return {"message": "There was an error uploading the file"}


    background_tasks.add_task(process_vid,filename)

    return {'message':'upload successfull'}

@app.get("/subsearch")
async def subsearch(name:str, text:str):
    container = get_database.get_container()
    #print(container)
    #print("text",text)
    #print("name",name)

    text = f'''"%{text}%"'''
    name = f'''"{name}"'''
    print("name",name)
    print("text",text)
    if not bool(name and text):
        print("empty query")
        return{"message":"enter valid query"}
    stamp_lis = query.get_time_stamp(name,text,container)
    return stamp_lis

@app.get("/heath")
async def health():
    return {"meassage":"success"}
