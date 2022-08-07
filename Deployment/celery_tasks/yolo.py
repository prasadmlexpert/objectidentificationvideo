import logging
import torch
import os
import cv2
import matplotlib.pyplot as plt


class YoloModel:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path= 'yolov5xbdd.pt' ,force_reload=True)
        self.model.eval()

    def predict(self, img):
        print("in processing --------------------------------------------------------")
        print(img)
        print(type(img))
        if img[-3:] == 'mp4':
            print("in processing --------------------------------------------------------1")
            vid = cv2.VideoCapture(img)

            try:
                print("in processing --------------------------------------------------------2")
                # creating a folder named data
                if not os.path.exists('data'):
                    os.makedirs('data')

            # if not created then raise error
            except OSError:
                print('Error: Creating directory of data')

            # frame
            currentframe = 0
            print("in processing --------------------------------------------------------3")

            while (True):

                # reading from frame
                success, frame = vid.read()
                print(f"in processing --------------------------------------------------------{3+currentframe}")
                if success:
                    # continue creating images until video remains
                    name = './data/frame' + str(currentframe) + '.jpg'
                    print('Creating...' + name)

                    # writing the extracted images
                    cv2.imwrite(os.path.join(os.getcwd(),name), frame)
                    with torch.no_grad():
                        result = self.model(os.path.join(os.getcwd(),name))
                        result.save('static/results/')

                    # increasing counter so that it will
                    # show how many frames are created
                    currentframe += 1
                else:
                    break
            print(f"in processing --------------------------------------------------------{3+currentframe}")
            data = []
            for i in range(len(result.xywhn[0])):
                x, y, w, h, prob, cls = result.xywhn[0][i].numpy()
                preds = {}
                preds['x'] = str(x)
                preds['y'] = str(y)
                preds['w'] = str(w)
                preds['h'] = str(h)
                preds['prob'] = str(prob)
                preds['class'] = result.names[int(cls)]
                data.append(preds)
            file_name = os.path.join(os.getcwd(),name)
            return {'file_name': file_name, 'bbox': data}

        else:
            try:
                with torch.no_grad():
                    result = self.model(img)
                result.save('static/results/')
                final_result = {}
                data = []
                file_name = f'static/{result.files[0]}'

                for i in range(len(result.xywhn[0])):
                    x, y, w, h, prob, cls = result.xywhn[0][i].numpy()
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