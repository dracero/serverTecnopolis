#Esta es la app que usa fastapi para hacer el chatbot con openai (o sea con chat GPT)
import openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Hay solo cinco dólares gratis de openai, así que no se puede usar mucho. Despés hay que pagar.
API_KEY = "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"
openai.api_key = API_KEY

app = FastAPI()

# Configuración de los orígenes permitidos (en este caso, cualquier origen)
origins = ["*"]

# Agregar middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(input_messages: list):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_messages,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    output_message = response.choices[0].text
    return {"response": output_message}