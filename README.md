<div align="center">
  <p>
    <a align="center" href="https://ultralytics.com/yolov5" target="_blank">
      <img width="850" src="https://github.com/ultralytics/assets/raw/master/yolov5/v62/splash_readme.png"></a>
  </p>
</div>

# Yolo V5 

<div align="center">
YOLOv5 🚀 is a family of object detection architectures and models pretrained on the COCO dataset, and represents Ultralytics open-source research into future vision AI methods, incorporating lessons learned and best practices evolved over thousands of hours of research and development.
</div>


Yolo maintainer github location - https://github.com/ultralytics/yolov5 <br/>
Yolo V5 Architecture - [link](https://github.com/ultralytics/yolov5/issues/6998)(Yolov5 paper not yet available)<br/>
How to Train Yolo V5 - [link](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)<br/>


# Training Yolo V5 [BDD Data set](https://bdd-data.berkeley.edu/)
## Convert BDD Data set Scalable json format to Yolo format
[BDD Data set](https://bdd-data.berkeley.edu/portal.html) comes with [Scalable json format](https://doc.scalabel.ai/format.html) , which needs to be converted to Yolo txt format.<br/>

This experiment is performed with [Detection 2020](https://doc.bdd100k.com/download.html#detection-2020-labels) lables.<br/>

To convert the json to yolo txt format use [bdd2yolotxt.py](https://github.com/prasadmlexpert/objectidentificationvideo/blob/main/bdd2yolotxt.py)<br/>

```
usage: bdd2yolotxt.py [-h] [-i IMAGEROOT] [-l LABLEPATH] [-o OUTPUTDIR] [-t TARGET] [-n NOOFEACHITEM]

options:
  -h, --help            show this help message and exit
  -i IMAGEROOT, --ImageRoot IMAGEROOT
                        ImageRoot
  -l LABLEPATH, --LablePath LABLEPATH
                        Labels path
  -o OUTPUTDIR, --OutputDir OUTPUTDIR
                        Output directory
  -t TARGET, --target TARGET
                        target items to be trained or validated file path
  -n NOOFEACHITEM, --noOfEachItem NOOFEACHITEM
                        Number of items to be extracted of each image type, 0 means all
```
 Re arrange the data set as described in https://github.com/prasadmlexpert/objectidentificationvideo/blob/main/yolov5reduced.yml <br/>
 final folder architecture after cloning yolov5<br/>
 ```
 images
 labels
 yolov5
 ```
 
 In order not to regenerate the folder structure, data is stored in zipped format, and saved to drive at [location](https://drive.google.com/file/d/19eofB_tGB0xX-Qrt0zmvXiYj2bMPP9B1/view?usp=sharing)
 
 ## Train model
 ### Example with Yolov5x
Traing model using [YoloV5CustomTrainingBDD100k.ipynb](https://github.com/prasadmlexpert/objectidentificationvideo/blob/498fc1eaea8cc169aac442b4851629be65e0f4ee/YoloV5CustomTrainingBDD100k.ipynb)<br/>

## Deployment
### GCP(google cloud)
Create a virtual machine using https://docs.ultralytics.com/environments/GCP-Quickstart/ <br/>
In the deployment virtual machine clone Project2022 <br/>
 ```
git clone https://github.com/gpvprasad/Project2022.git
pip3 install -r requirements.txt 
cd Project2022
gdown <link to pre trained model, currently supported yolo 5l and 5x>
python server.py --port 8080
 ```
 <table>
 <tr>
    <th>Yolo5l BDD trained</th>
    <th>Yolo5x BDD trained</th>
  </tr>
  <tr>
    <td>
     <p>
      <a align="center">
        <img width=60% height=auto src="https://github.com/prasadmlexpert/objectidentificationvideo/raw/main/yolo5lcustom.jpg"></a>
     </p>
    </td>
    <td>
     <p>
      <a align="center">
        <img width=700% height=auto src="https://github.com/prasadmlexpert/objectidentificationvideo/raw/main/yolo5xcustom.jpg"></a>
     </p>
    </td>
  </tr>
  </table>
  
  
### Deployment docker(gcp) 
```
Not explored on GCP works on local
```

built using https://github.com/GoldVelvet/YOLOv5-fastapi-celery-redis-rabbitmq <br/>
Run on GCP <br/>
```
git clone https://github.com/prasadmlexpert/objectidentificationvideo.git
cd objectidentificationvideo/Deployment
gdown <yolov5xbdd pretrained model>
docker-compose build
docker-compose up &
cd webapp
uvicorn app:app --host 0.0.0.0 --port 80 --reload
```



## <div align="center">Environments</div>

Get started in seconds with our verified environments. Click each icon below for details.

<div align="center">
  <a href="https://github.com/prasadmlexpert/objectidentificationvideo/blob/main/YoloV5CustomTrainingBDD100k.ipynb">
    <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-colab-small.png" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/master/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://hub.docker.com/r/ultralytics/yolov5">
    <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-docker-small.png" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/master/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://github.com/ultralytics/yolov5/wiki/GCP-Quickstart">
    <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-gcp-small.png" width="10%" /></a>
</div>

