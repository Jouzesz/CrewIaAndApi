from crewai import Task
from agents import chef, culturalista, escritor

tarefa_receita = Task(
    description="Com base no ingrediente fornecido, encontre uma receita internacional típica.",
    expected_output="Nome do prato, país de origem, ingredientes e modo de preparo.",
    agent=chef
)

tarefa_contexto = Task(
    description="Forneça um breve contexto cultural e histórico do país da receita.",
    expected_output="Informações culturais do país e curiosidades gastronômicas.",
    agent=culturalista,
    context=[tarefa_receita]
)

tarefa_redacao = Task(
    description="Escreva uma receita detalhada combinando os dados da receita e do contexto cultural, em português claro e acessível.",
    expected_output="Texto completo da receita.",
    agent=escritor,
    context=[tarefa_receita, tarefa_contexto],
    output_file="output/receita_final.md"
)