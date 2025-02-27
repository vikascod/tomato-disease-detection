from fastapi import FastAPI
import uvicorn
from .routes import predict

app = FastAPI()

app.include_router(predict.router)

@app.get("/")
def home():
    return {"message": "Tomato Disease Classification API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
