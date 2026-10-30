import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_PATH = BASE_DIR / "data" / "knowledge" / "competencias.json"


def carregar_competencias():
    with open(KNOWLEDGE_PATH, encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["competencias"]


def buscar_competencia(consulta, competencias):
    consulta = consulta.lower().strip()

    for competencia in competencias:
        assunto = competencia["assunto"].replace("_", " ")

        if assunto in consulta:
            return competencia

        for termo in competencia.get("termos", []):
            if termo.lower() in consulta:
                return competencia

    return None

def identificar_tema(consulta, tema):
    consulta = consulta.lower().strip()

    for termo in tema.get("termos", []):
        if termo.lower() in consulta:
            return True

    return False

def exibir_competencia(competencia):
    fundamento = competencia["fundamento"]

    print("\n--- Quem Decide? ---")
    print(f"Assunto: {competencia['assunto']}")
    print(f"Órgão: {competencia['orgao']}")
    print(f"Ente: {competencia['ente']}")
    print(f"Relação: {competencia['relacao']}")

    print(
        "Fundamento: "
        f"{fundamento['norma']}, "
        f"art. {fundamento['artigo']}, "
        f"§ {fundamento['paragrafo']}"
    )

    if "observacao" in competencia:
        print(f"Observação: {competencia['observacao']}")


def main():
    with open(KNOWLEDGE_PATH, encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    competencias = dados["competencias"]
    tema = dados["tema"]

    consulta = input("Digite sua pergunta: ").strip()

    resultado = buscar_competencia(consulta, competencias)

    if resultado:
        exibir_competencia(resultado)

    elif identificar_tema(consulta, tema):
        print(f"\nSua pergunta envolve: {tema['nome']}.")
        print("Esse tema possui diferentes competências institucionais.")
        print("\nVocê pode perguntar sobre:")

        for competencia in competencias:
            assunto = competencia["assunto"].replace("_", " ")
            print(f"- {assunto}")

    else:
        print("\nAinda não encontrei informações suficientes na minha base.")


if __name__ == "__main__":
    main()