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

        if consulta == assunto:
            return competencia

        for termo in competencia.get("termos", []):
            if consulta == termo.lower():
                return competencia

    return None


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
    competencias = carregar_competencias()

    assunto = input("Digite o assunto que deseja consultar: ").strip()

    resultado = buscar_competencia(assunto, competencias)

    if resultado:
        exibir_competencia(resultado)
    else:
        print("\nCompetência não encontrada.")


if __name__ == "__main__":
    main()