from langchain_groq import ChatGroq;
from dotenv import load_dotenv;
import os;

# Usando o load_dotenv para carregar os dados da API
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

numero_de_dias = 7;
numero_de_criancas = 2;
atividade = "praia";

prompt = f"crie um roteiro de viagem de {numero_de_dias} com {numero_de_criancas} crianças, que gostam de {atividade}."


llm = ChatGroq(api_key = api_key, model="llama3-8b-8192")

resposta = llm.invoke(prompt)

print(resposta.content)
