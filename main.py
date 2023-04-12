#llamarlo con esto uvicorn main:app --port 8000 --host 0.0.0.0 --reload
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
from transformers import pipeline

app = FastAPI()

# Permitir solicitudes desde cualquier origen
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/image-to-text")
async def image_to_text(file: UploadFile = File(...)):
    # Cargar el modelo
    image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

    # Leer la imagen y pasarla al modelo para obtener el texto
    contents = await file.read()
    image = Image.open(BytesIO(contents))
    text = image_to_text(image)

    # Devolver el texto como respuesta
    return {"text": text[0]["generated_text"]}

