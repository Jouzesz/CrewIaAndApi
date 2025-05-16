import os
from crewai import Agent
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="groq/llama3-70b-8192",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.6
)

chef = Agent(
    role="Chef Virtual",
    goal="Criar receitas detalhadas com base no ingrediente",
    backstory="Você é um chef expert que cria receitas incríveis.",
    verbose=True,
    llm=llm,
    allow_delegation=False
)

culturalista = Agent(
    role="Especialista Cultural",
    goal="Fornecer contexto cultural e histórico da receita",
    backstory="Você é um especialista em culturas gastronômicas do mundo.",
    verbose=True,
    llm=llm,
    allow_delegation=False
)

escritor = Agent(
    role="Redator de Conteúdo",
    goal="Escrever textos explicativos e envolventes sobre receitas e cultura",
    backstory="Você escreve artigos para blogs culinários com linguagem acessível.",
    verbose=True,
    llm=llm,
    allow_delegation=False
)