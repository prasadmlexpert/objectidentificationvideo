import torch
from azureml.core import Model
import json
def init():

    global model

    model_name = 'bddyolov5'

    path = Model.get_model_path(model_name)

    model = torch.hub.load('ultralytics/yolov5', 'custom', path= path ,force_reload=True)
    model.eval()

def run(data):

    try:

        data = json.loads(data)

        result = model(data['data'])
        result.render()

        return {'data' : result.imgs[0] , 'message' : "classified"}

    except Exception as e:

        error = str(e)

        return {'data' : error , 'message' : 'Failed to classify'}
