from knowledge import carregar_competencias
from interpreter import buscar_competencia, identificar_tema


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
    dados = carregar_competencias()

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