import cv2
cv2.namedWindow('imageWindow')
import numpy as np

img = cv2.imread('/Users/shravanchandu/Documents/AIML_IIITH/git/objectidentificationvideo/Testing/b1c66a42-6f7d68ca.jpg')
img_height = img.shape[0]
img_width = img.shape[1]

class_labels = ['car', 'truck', 'bus', 'train', 'person', 'rider', 'traffic sign', 'traffic light', 'motorcycle', 'pedestrian', 'bicycle', 'other vehicle', 'trailer', 'other person']

with open("/Users/shravanchandu/Documents/AIML_IIITH/git/objectidentificationvideo/Testing/b1c66a42-6f7d68ca.txt",'r',encoding = 'utf-8') as f:
    #print(f.read().split())
    for line in f:
        print(line.split())
        lst = line.split()
        start_point = (int((float(lst[1])-float(lst[3])/2)*img_width), int((float(lst[2])-float(lst[4])/2)*img_height))
        end_point = (int((float(lst[1])+float(lst[3])/2)*img_width), int((float(lst[2])+float(lst[4])/2)*img_height))
        color = (255, 0, 0)
        thickness = 2
        img = cv2.rectangle(img, start_point, end_point, color, thickness)

        font = cv2.FONT_HERSHEY_SIMPLEX

        # org
        org = start_point
        # fontScale
        fontScale = 1

        # Blue color in BGR
        color = (128, 128, 128)

        # Line thickness of 2 px
        thickness = 2

        # Using cv2.putText() method
        img = cv2.putText(img, class_labels[int(lst[0])], org, font,fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow('imageWindow',img)
wait = True
while wait:
    wait = cv2.waitKey()=='q113' # hit q to exit

#cv2.rectangle(img,(x,y),(x1,y1),(0,255,0),2)



