from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from google.colab.patches import cv2_imshow

app = FastAPI()


@app.get("/hello")
def root():
    return {"message": "Fast API in Python 123"}

#file: UploadFile = File(description="A file read as UploadFile")

@app.post('/uploadfile')
def _file_upload(my_file: UploadFile = File(...)):
  print('hello')
  //1. read the image-file and view
  img_to_detect = cv2.imread('images/10k/train/004071a4-049be89b.jpg')
  img_height = img_to_detect.shape[0]
  img_width = img_to_detect.shape[1]
  img_blob = cv2.dnn.blobFromImage(img_to_detect, 0.003922, (416, 416), swapRB=True, crop=False)

  //2. call the pre-trained model function
  calculateConfidence(img_blob) 
  
  //3. return the taged image
  tagged_img = predictions()

  cv2_imshow(tagged_img)
  cv2.imwrite("results.jpg", tagged_img)

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



