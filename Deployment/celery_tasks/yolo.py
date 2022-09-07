import logging
import torch
import os
import cv2
import matplotlib.pyplot as plt
import gc
import ffmpeg    

def check_rotation(path_video_file):
    # this returns meta-data of the video file in form of a dictionary
    meta_dict = ffmpeg.probe(path_video_file)

    # from the dictionary, meta_dict['streams'][0]['tags']['rotate'] is the key
    # we are looking for
    rotateCode = None
    if int(meta_dict['streams'][0]['tags']['rotate']) == 90:
        rotateCode = cv2.ROTATE_90_CLOCKWISE
    elif int(meta_dict['streams'][0]['tags']['rotate']) == 180:
        rotateCode = cv2.ROTATE_180
    elif int(meta_dict['streams'][0]['tags']['rotate']) == 270:
        rotateCode = cv2.ROTATE_90_COUNTERCLOCKWISE

    return rotateCode

def correct_rotation(frame, rotateCode):  
    return cv2.rotate(frame, rotateCode) 
class YoloModel:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path= 'yolov5xbdd.pt' ,force_reload=True)
        self.model.eval()

    def predict(self, img):
        print("in processing --------------------------------------------------------")
        print(img)
        print(type(img))
        if img[-3:] == 'mp4' or img[-3:] == 'mov':
            print("in processing --------------------------------------------------------1")
            vid = cv2.VideoCapture(img)
            outpath = os.path.join(os.getcwd(),"./api/static/video.mp4")
            if img[-3:] == 'mov':
                rotateCode = check_rotation(img)

            try:
                print("in processing --------------------------------------------------------2")
                # creating a folder named data
                if not os.path.exists('data'):
                    os.makedirs('data')
                print(os.getcwd())
                size = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
                print(size)
                print(vid.get(cv2.CAP_PROP_FPS))
                videowriter = cv2.VideoWriter(outpath, cv2.VideoWriter_fourcc(*'mp4v') , 30 , size)

            # if not created then raise error
            except OSError:
                print('Error: Creating directory of data')

            # frame
            currentframe = 0
            print("in processing --------------------------------------------------------3")

            while (True):

                # reading from frame
                success, frame = vid.read()
                print(success)
                if img[-3:] == 'mov':
                    if rotateCode is not None:
                        frame = correct_rotation(frame, cv2.ROTATE_180)
                print(f"in processing --------------------------------------------------------{3+currentframe}")
                if success  :
                    
                    with torch.no_grad():
                        result = self.model(frame)
                        result.render()
                        print(result)
                        videowriter.write(result.ims[0])
                        # result.save(save_dir='static/results/')
                        

                    # increasing counter so that it will
                    # show how many frames are created
                    currentframe += 1
                else:
                    break
            print(f"in processing --------------------------------------------------------{3+currentframe}")
            vid.release()
            videowriter.release()
            data = []
            for i in range(len(result.xywhn[0])):
                preds = {}
                preds['x'] = 'video'
                preds['y'] = 'video'
                preds['w'] = 'video'
                preds['h'] = 'video'
                preds['prob'] = 'video'
                preds['class'] = 'video'
                data.append(preds)
            del vid
            gc.collect()
            return {'file_name': 'static/video.mp4', 'bbox': data}

        else:
            try:
                with torch.no_grad():
                    result = self.model(img)
                result.save(save_dir='api/static/')
                final_result = {}
                data = []
                file_name = f'static/{result.files[0]}'

                for i in range(len(result.xywhn[0])):
                    x, y, w, h, prob, cls = result.xywhn[0][i].cpu().numpy()
                    preds = {}
                    preds['x'] = str(x)
                    preds['y'] = str(y)
                    preds['w'] = str(w)
                    preds['h'] = str(h)
                    preds['prob'] = str(prob)
                    preds['class'] = result.names[int(cls)]
                    data.append(preds)

                return {'file_name': file_name, 'bbox': data}
            except Exception as ex:
                logging.error(str(ex))
                return None
