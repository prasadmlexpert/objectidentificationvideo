import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
from tqdm import tqdm
import cv2
imgRootPath = None
labelPath = None
outDir = None
numberofItems = 0
import argparse
# list of command line arguments
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--ImageRoot", help = "ImageRoot")
parser.add_argument("-l", "--LablePath", help = "Labels path")
parser.add_argument("-o", "--OutputDir", help = "Output directory")
parser.add_argument("-t", "--target", help = "target items to be trained or validated file path")
parser.add_argument("-n", "--noOfEachItem",type=int, help = "Number of items to be extracted of each image type, 0 means all")
args = vars(parser.parse_args())
print(args['ImageRoot'],args['LablePath'],args['OutputDir'],args['noOfEachItem'],args['target'])

counter = {'car': 0, 'truck': 1, 'bus': 2, 'train': 3, 'person': 4, 'rider': 5, 'traffic sign': 6, 'traffic light': 7, 'motorcycle': 8, 'pedestrian': 9, 'bicycle': 10, 'other vehicle': 11, 'trailer': 12, 'other person': 13}

lastidentifier = 13
def classify_classes(c_name):
    vehicle = ["car", "truck", "bus", "train"]
    if c_name in vehicle:
        return 0
    else:
        return 1


def convert2yolo_roi(img_name, obj):

    obj_name = obj["category"]
    obj_class = counter[obj_name]
    obj_roi = obj['box2d']

    img = cv2.imread(img_name)
    img_w, img_h = img.shape[1], img.shape[0]

    w = (obj_roi["x2"] - obj_roi["x1"])
    h = (obj_roi["y2"] - obj_roi["y1"])
    x = (obj_roi["x1"] + w/2)
    y = (obj_roi["y1"] + h/2)

    x, y, w, h = x/img_w, y/img_h, w/img_w, h/img_h

    return "{} {} {} {} {}\n".format(obj_class, x, y, w, h)

def parseline(line,items,finalFile):
    global lastidentifier
    name = line['name']
    imgPath = imgRootPath + name
    txtPath = imgPath.replace("jpg", "txt")
    if os.path.isfile(imgPath):
        with open(txtPath, "w")as file:
            if 'labels' in line.keys():
                labels = line['labels']
                for label in labels:
                    category = label["category"]
                    if category in counter.keys():
                        file.write(convert2yolo_roi(imgPath, label))
                    else:
                        lastidentifier +=1
                        counter[category] = lastidentifier
                        file.write(convert2yolo_roi(imgPath, label))
                        print(txtPath)
                        print(counter)
            file.close()
        with open(finalFile,"a") as file:
            file.writelines("data/obj/"+name+"\n")
            file.close()

if __name__ == '__main__':
    imgRootPath = args['ImageRoot']
    labelPath = args['LablePath']
    outdir = args['OutputDir']
    itemsoftype = args['noOfEachItem']
    
    with open(labelPath) as labelFile:
        lines = json.load(labelFile)

    with open(labelPath) as labelFile:
        lines = json.load(labelFile)

    with tqdm(total=len(lines)) as pbar:
        with ThreadPoolExecutor(max_workers=100) as ex:
            futures = [ex.submit(parseline, line,itemsoftype,args['target']) for line in lines]
            
            for future in as_completed(futures):
                result = future.result()
                pbar.update(1)

    print("line_num : {}".format(len(lines)))
