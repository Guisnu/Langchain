from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain.chains.sequential import SimpleSequentialChain
from langchain import LLMChain
from langchain.globals import set_debug
import os

from langchain_core.pydantic_v1 import Field, BaseModel

class Destino(BaseModel):
    cidade = Field("Cidade a visitar")
    motivo = Field("Motivo pelo qual é interressante visitar")

set_debug(True)

# Carregar as variáveis de ambiente
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Configuração do modelo LLM (Groq)
llm = ChatGroq(
    api_key=api_key,
    temperature=0.5,
    model="llama3-8b-8192",
)

parseador = JsonOutputParser(pydantic_object=Destino)

modelo_cidade = PromptTemplate(
    template="""Sugira uma cidade baseado no meu interesse por {interesse}.
    {formatacao_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()}
)

modelo_restaurantes = ChatPromptTemplate.from_template(
    "Sugira restaurantes populares entre locais em {cidade}"
)

modelo_cultural = ChatPromptTemplate.from_template(
    "Sugira atividades culturais locais em {cidade}"
)

cadeia_cidade = LLMChain(prompt = modelo_cidade, llm = llm )
cadeia_restaurantes = LLMChain(prompt = modelo_restaurantes, llm = llm )
cadeia_cultural = LLMChain(prompt = modelo_cultural, llm = llm )

cadeia = SimpleSequentialChain(chains=[cadeia_cidade], verbose=True)

response = cadeia.invoke("praia")
