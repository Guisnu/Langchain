from langchain_groq import ChatGroq;
from dotenv import load_dotenv;
import os;

numero_de_dias = 7;
numero_de_criancas = 2;
atividade = "praia";

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key = api_key,
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    )

system = "Você é um assistente útil."
human = f"crie um roteiro de viagem de {numero_de_dias} com {numero_de_criancas} crianças, que gostam de {atividade}."

prompt = [
    ("system",system,),
    ("human", human),
]

ai_msg = llm.invoke(prompt)

print(ai_msg.content)