import cv2
import os

path=input(str("enter path:"))
out_path= path
out_video_name="video.mp4"
out_video_full_path=out_path+out_video_name


import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

pre_imgs= sorted_alphanumeric(os.listdir(path))
#print(pre_imgs)
img=[]

for i in pre_imgs:
    i=path+i
    #print(i)
    img.append(i)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

size =(1280,720)


video= cv2.VideoWriter(out_video_full_path, cv2_fourcc, 30, size)  #videoName, fourcc, fps, size

for i in range(len(img)):
    video.write(cv2.imread(img[i]))

video.release()
