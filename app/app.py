from fastapi import FastAPI, File, UploadFile
import numpy as np
import io
from PIL import Image
from tensorflow import keras

app = FastAPI()

model = keras.models.load_model('tomato_disease.h5')

def read_image(image):
    img = Image.open(io.BytesIO(image))
    img = img.resize((256, 256))
    img = np.array(img)
    return img

@app.get('/')
async def home():
    return "Welcome to tomato diease detection app"


@app.post('/detect')
async def detect(file:UploadFile=File(...)):
    image = read_image(await file.read())
    # Add batch dimension
    img = np.expand_dims(image, axis=0)
    # Prediction
    prediction = model.predict(img)

    pred = np.argmax(prediction.tolist())

    class_labels = ['Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold',
                'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two_spotted_spider_mite',
                'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus',
                'Tomato_healthy']
    
    # Find the confidence probability
    confidence = float(np.max(prediction[0]))

    predicted_class = class_labels[pred]
    return {"prediction": predicted_class, "confidence": confidence}