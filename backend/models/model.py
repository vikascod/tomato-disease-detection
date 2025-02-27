import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img


# Load Model
model = tf.keras.models.load_model("model_training/tomato_disease.h5")

# Class Labels
class_labels = ['Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight',
                'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
                'Tomato_Spider_mites_Two_spotted_spider_mite',
                'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus',
                'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']


def predict_image(image_path):
    img = load_img(image_path, target_size=(256, 256))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    pred_index = np.argmax(prediction)
    confidence = prediction[0][pred_index]

    return class_labels[pred_index], float(confidence)
