from groq import Groq;
from dotenv import load_dotenv;
import os;

# Usando o load_dotenv para carregar os dados da API
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

numero_de_dias = 7;
numero_de_criancas = 2;
atividade = "praia";

prompt = f"crie um roteiro de viagem de {numero_de_dias} com {numero_de_criancas} crianças, que gostam de {atividade}."

#definindo que o prompt será passado pela função getprompt()
client = Groq(
    api_key=os.environ.get(api_key),
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f'{prompt}',
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)