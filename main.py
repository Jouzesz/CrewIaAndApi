import os
import re
from crewai import Crew
from tasks import tarefa_receita, tarefa_contexto, tarefa_redacao
import tools

def main():
    os.makedirs("output", exist_ok=True)
    ingrediente = input("Digite o ingrediente principal: ")

    # 1. Buscar dados
    receita = tools.busca_receita(ingrediente)
    if "erro" in receita:
        print(receita["erro"])
        return
    print(f"Receita encontrada: {receita['strMeal']} - {receita['strArea']}")
    pais = receita['strArea']
    contexto = tools.info_pais(pais)

    # 2. Inserir os dados nos descriptions
    tarefa_receita.description = f"Crie uma descrição da receita a seguir, incluindo nome do prato, país de origem, ingredientes e modo de preparo:\n\n{receita}"
    tarefa_contexto.description = f"Com base na seguinte informação cultural: {contexto}, e na receita: {receita['strMeal']} do país {pais}, escreva um breve histórico e curiosidades sobre a culinária do país."
    tarefa_redacao.description = (
        f"Combine os dados da receita '{receita['strMeal']}' com o contexto cultural de {pais} "
        f"para escrever uma receita detalhada e culturalmente contextualizada em português claro.\n\n"
        f"Receita: {receita}\n\nContexto: {contexto}"
    )

    # 3. Criar a crew e rodar
    crew = Crew(
        agents=[tarefa_receita.agent, tarefa_contexto.agent, tarefa_redacao.agent],
        tasks=[tarefa_receita, tarefa_contexto, tarefa_redacao],
        verbose=True
    )

    print("\n⏳ Processando com agentes...")
    resultado = crew.kickoff()

    # Traduzir resultado final
    print("\n🌍 Traduzindo resultado final para o português...")
    traduzido = tools.traduzir_texto(str(resultado))

    with open("output/receita_final.md", "w", encoding="utf-8") as f:
        f.write(traduzido)


    print("\n📝 Receita final traduzida e salva em output/receita_final.md")
    print(traduzido)


if __name__ == "__main__":
    main()
