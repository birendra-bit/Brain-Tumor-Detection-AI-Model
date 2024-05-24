import streamlit as st 
from io import StringIO
from PIL import Image
import os
from datetime import datetime
from tensorflow.keras.applications.resnet50 import ResNet50
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
from tensorflow.keras.preprocessing import image

# Preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def make_prediction(img_path):
    # # Load pretrained model (instead of training the model for 1+ hours)
    # with open('classifier-resnet-model.json', 'r') as json_file:
    #     json_savedModel= json_file.read()
        
    # # load the model
    # model = tf.keras.models.model_from_json(json_savedModel)
    # model.load_weights('classifier-resnet-weights.keras')
    # model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics= ["accuracy"])

    model = tf.keras.models.load_model('classifier-resnet-weights.keras')
    
    img_array = preprocess_image(img_path)
    predict_image = model.predict(img_array)
    return predict_image[0][0] 

