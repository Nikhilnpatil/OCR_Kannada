import tensorflow as tf
import numpy as np
from app.kannada.characters import CHARACTERS

model=tf.keras.models.load_model("app/models/model2.h5")

def get_kannada_prediction(data: np.array) -> str:
    '''get_kannada_prediction(data) takes the image data in the required format and returns the string of predicted character'''
    result = model.predict(data)
    position = 0
    probability_max = 0
    for index in range(0,len(result[0])):
        if result[0][index] > probability_max:
            probability_max = result[0][index]
            position = index
    return CHARACTERS[position].decode('utf-8')

