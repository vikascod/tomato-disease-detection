from fastapi import FastAPI, File, UploadFile
import numpy as np
import io
from PIL import Image
from tensorflow import keras

app = FastAPI()

model = keras.models.load_model('app/tomato_disease.h5')

def read_image(image):
    img = Image.open(io.BytesIO(image))
    img = img.resize((256, 256))
    img = np.array(img)
    return img

disease_prevention = {
    "Tomato_Bacterial_spot": [
        "Prevent bacterial spot by using disease-free seeds.",
        "Implement crop rotation to reduce the disease's prevalence.",
        "Apply copper-based fungicides to control the disease."
    ],
    "Tomato_Early_blight": [
        "Prevent early blight by practicing good garden hygiene.",
        "Ensure proper watering to avoid splashing soil onto the leaves.",
        "Apply fungicides as needed to control the disease."
    ],
    "Tomato_Late_blight": [
        "Prevent late blight by providing good air circulation in your garden or greenhouse.",
        "Avoid overhead watering, as wet leaves can encourage the disease.",
        "Apply fungicides when necessary to manage the disease."
    ],
    "Tomato_Leaf_Mold": [
        "Prevent leaf mold by ensuring good air circulation and spacing between plants.",
        "Avoid wetting the leaves when watering, and water the soil instead.",
        "Apply fungicides if the disease is present and worsening."
    ],
    "Tomato_Septoria_leaf_spot": [
        "Prevent Septoria leaf spot by maintaining good garden hygiene.",
        "Avoid overhead watering to keep the leaves dry.",
        "Apply fungicides if the disease becomes a problem."
    ],
    "Tomato_Spider_mites_Two_spotted_spider_mite": [
        "Prevent spider mite infestations by regularly inspecting your plants for signs of infestation.",
        "Increase humidity in the growing area to discourage mites.",
        "Use insecticidal soap or neem oil to control mites if necessary."
    ],
    "Tomato__Target_Spot": [
        "Prevent target spot by ensuring good air circulation and avoiding overcrowding of plants.",
        "Water at the base of the plants, keeping the leaves dry.",
        "Apply fungicides as needed to control the disease."
    ],
    "Tomato__Tomato_YellowLeaf__Curl_Virus": [
        "Prevent Tomato Yellow Leaf Curl Virus by using virus-free tomato plants.",
        "Control whiteflies, which transmit the virus, with insecticides.",
        "Remove and destroy infected plants to prevent the spread of the disease."
    ],
    "Tomato__Tomato_mosaic_virus": [
        "Prevent tomato mosaic virus by using virus-free seeds and disease-resistant tomato varieties.",
        "Control aphids, which transmit the virus, with insecticides.",
        "Remove and destroy infected plants to prevent further spread."
    ],
    "Tomato_healthy": [
        "If your tomato plant is healthy, continue to monitor for pests and diseases regularly.",
        "Follow good gardening practices, including proper watering, fertilization, and maintenance."
    ]
}


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

    # Get the prevention measures for the predicted disease
    prevention_measures = disease_prevention.get(predicted_class, 'Prevention measures not available for this disease.')

    response = {
        "prediction": predicted_class,
        "confidence": confidence,
        "prevention_measures": prevention_measures
    }

    return response