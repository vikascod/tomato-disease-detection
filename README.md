# Tomato Disease Detector App

Welcome to the Tomato Disease Detector. This FastAPI-based application is designed to help you identify the health status of tomato plants. By uploading an image of a tomato plant's leaves, you can receive predictions about whether the plant is healthy or if it is suffering from one of several common diseases.

## Prerequisites

Before running the Tomato Disease Detector API, ensure that you have the following components installed on your system:

- Python (version 3.7 or later)
- TensorFlow (for deep learning)
- FastAPI (for creating the API)
- Uvicorn (for running the FastAPI application)
- Pillow (PIL, for image processing)
- NumPy (for numerical operations)

# You can install the dependencies from the `requirements.txt` file using the following command:

    ```bash
    pip install -r requirements.txt

## Run the FastAPI Application

To start the Tomato Disease Detector API, navigate to the directory containing your FastAPI application code and run the following command:

    ```bash
    uvicorn app.app:app --reload
    
## Using the Tomato Disease Detector

To use the Tomato Disease Detector, follow these steps:

Access the API: Open your web browser and navigate to the API endpoint (e.g., http://localhost:8000).

Upload an Image: Click the "Upload" button to select an image of tomato plant leaves from your device.

Get Predictions: Once you've uploaded the image, click the "Detect Disease" button. The application will analyze the image and provide predictions.

## Interpretation of Results

The Tomato Disease Detector App will provide you with a JSON response containing the following information:

- `"prediction"`: This field indicates the predicted class, which can be one of the following:

  - `"Tomato_Bacterial_spot"`: Indicates the presence of Bacterial Spot disease.
  - `"Tomato_Early_blight"`: Indicates the presence of Early Blight disease.
  - `"Tomato_Late_blight"`: Indicates the presence of Late Blight disease.
  - `"Tomato_Leaf_Mold"`: Indicates the presence of Leaf Mold disease.
  - `"Tomato_Septoria_leaf_spot"`: Indicates the presence of Septoria Leaf Spot disease.
  - `"Tomato_Spider_mites_Two_spotted_spider_mite"`: Indicates the presence of Spider Mites disease.
  - `"Tomato__Target_Spot"`: Indicates the presence of Target Spot disease.
  - `"Tomato__Tomato_YellowLeaf__Curl_Virus"`: Indicates the presence of Yellow Leaf Curl Virus.
  - `"Tomato__Tomato_mosaic_virus"`: Indicates the presence of Mosaic Virus.
  - `"Tomato_healthy"`: Indicates that the tomato plant appears to be healthy.

- `"confidence"`: This field provides a floating-point value representing the confidence level of the prediction. It indicates how certain the model is about its prediction, with higher values indicating greater confidence.

Example JSON response:

```json
{
    "prediction": "Potato___Early_blight",
    "confidence": 0.873
}