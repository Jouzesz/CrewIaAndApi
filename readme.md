#Projeto de receitas com IA

Funcionalidades
- Busca receitas estrangeiras a partir de um ingrediente principal.
- Fornece um contexto cultural do país de origem da receita.
- Gera uma receita completa com ingredientes e como preparar.
- Traduz o texto final para português.
- Salva o resultado em um arquivo `.md`.

Tecnologias e APIs
CrewAI + LangChain + Groq
- Criação de agentes inteligentes com **objetivos específicos**.
- Utiliza o modelo LLaMA3 (via Groq) para geração de texto.

- **[TheMealDB](https://www.themealdb.com/api.php)** – Para obter receitas com base em ingredientes.
- **[REST Countries](https://restcountries.com/)** – Para obter informações culturais e geográficas dos países.
- **[MyMemory Translator](https://mymemory.translated.net/doc/spec.php)** – Para traduzir o conteúdo final automaticamente para português (tem um limite de 500 caracteres por requisição e 100 traduções diárias).


