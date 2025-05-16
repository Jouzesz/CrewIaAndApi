import time
import requests

ingredientes_mapeados = {
    "frango": "chicken",
    "carne": "beef",
    "porco": "pork",
    "ovo": "egg",
    "batata": "potato",
    "arroz": "rice",
    "tomate": "tomato",
    "queijo": "cheese",
    "peixe": "fish",
    "massa": "pasta",
    "milho": "corn"
}


def busca_receita(ingrediente: str) -> dict:
    ingrediente_en = ingredientes_mapeados.get(ingrediente.lower(), ingrediente)
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingrediente_en}"
    res = requests.get(url)
    data = res.json()
    if not data['meals']:
        return {"erro": f"Nenhuma receita encontrada para '{ingrediente}'."}
    meal = data['meals'][0]
    detalhe = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal['idMeal']}").json()
    return detalhe['meals'][0]


def info_pais(pais: str) -> dict:
    substituicoes = {
        "Jamaican": "Jamaica",
        "American": "United States",
        "British": "United Kingdom",
        "Canadian": "Canada",
        "Chinese": "China",
        "Indian": "India",
        "French": "France",
        "Italian": "Italy",
        "Spanish": "Spain",
        "Mexican": "Mexico",
        "Moroccan": "Morocco",
        "Thai": "Thailand",
        "Vietnamese": "Vietnam",
        "Turkish": "Turkey",
        "Russian": "Russia"
    }

    pais_cor = substituicoes.get(pais.strip(), pais.strip())

    res = requests.get(f"https://restcountries.com/v3.1/name/{pais_cor}")
    if res.status_code != 200:
        return {"erro": f"País '{pais_cor}' não encontrado na API."}
    data = res.json()[0]
    return {
        "nome": data.get("name", {}).get("common", "Desconhecido"),
        "capital": data.get("capital", ["N/A"])[0],
        "idioma": list(data.get("languages", {}).values())[0] if data.get("languages") else "N/A",
        "moeda": list(data.get("currencies", {}).keys())[0] if data.get("currencies") else "N/A"
    }

def traduzir_texto(texto: str, destino: str = "PT-BR") -> str:
    url = "https://api.mymemory.translated.net/get"
    partes = [texto[i:i+500] for i in range(0, len(texto), 500)]
    traduzido = ""

    for parte in partes:
        params = {
            "q": parte,
            "langpair": f"EN|{destino}"
        }
        res = requests.get(url, params=params)
        if res.status_code != 200:
            traduzido += f"[ERRO: {res.text}]"
            continue
        data = res.json()
        traduzido += data.get("responseData", {}).get("translatedText", parte)
        time.sleep(1.2)

    return traduzido
