import yolov5
import torch
import cv2

########################################################################################
model = yolov5.load('yolov5xbdd.pt')
mps_device = torch.device("mps")
model.to(mps_device)
vid = cv2.VideoCapture(0)
while True:
    ret, frame = vid.read()
    frame = mps_device
