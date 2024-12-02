from langchain_groq import ChatGroq;
from dotenv import load_dotenv;
from langchain_core.prompts import PromptTemplate
import os;

numero_de_dias = 7;
numero_de_criancas = 2;
atividade = "praia";

modelo_Prompt = PromptTemplate.from_template("crie um roteiro de viagem de {numero_de_dias} com {numero_de_criancas} crianças, que gostam de {atividade}.")

prompt = modelo_Prompt.format(numero_de_dias=numero_de_dias, numero_de_criancas=numero_de_dias, atividade=atividade)

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

ai_msg = llm.invoke(prompt)

print(ai_msg.content)