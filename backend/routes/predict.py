from fastapi import APIRouter, UploadFile, File
import shutil
from backend.models.model import predict_image


router = APIRouter()

@router.post("/predict/")
async def predict(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    predicted_class, confidence = predict_image(file_path)
    return {"class": predicted_class, "confidence": confidence}
