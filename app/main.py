from fastapi import FastAPI, HTTPException, File, UploadFile, Form

app = FastAPI()


@app.get("/hello")
def root():
    return {"message": "Fast API in Python"}


@app.post('/uploadfile')
def _file_upload(my_file: UploadFile = File(...)):
  print('hello')
  cv2_imshow(my_file)
  return {
      "name": my_file,
      "first": first
      }

@app.post("/files/")
async def create_file(file: bytes = File(...)):
  print('hello, inside create_file')
  return {"file_size": len(file)}



@app.post("/uploadfile2/")
async def create_upload_file(file: UploadFile):
  print('hello, inside create_upload_file')  
  return {"filename": file}

