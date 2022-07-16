from fastapi import FastAPI, HTTPException, File, UploadFile, Form

app = FastAPI()


@app.get("/hello")
def root():
    return {"message": "Fast API in Python 123"}

#file: UploadFile = File(description="A file read as UploadFile")

@app.post('/uploadfile')
def _file_upload(my_file: UploadFile = File(...)):
  print('hello')
  //1. read the image-file and view
  //2. call the pre-trained model function 
  //3. return the taged image
  return {
      "name"
      }

@app.post("/files")
async def create_file(file: bytes = File(...)):
  print('hello, inside create_file')
  return {"file_size": len(file)}



@app.post("/uploadfile2")
async def create_upload_file(image: UploadFile):
  print('hello, inside create_upload_file')  
  return {"filename"}



