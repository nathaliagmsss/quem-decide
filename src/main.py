from responses import responder_tramitacao
from knowledge import (
    carregar_competencias,
    buscar_proposicao,
    buscar_fonte,
)
from interpreter import (
    buscar_competencia,
    identificar_tema,
    identificar_intencao,
    identificar_proposicao,
)

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

    intencao = identificar_intencao(consulta)

    if intencao == "tramitacao":
        proposicao_id = identificar_proposicao(consulta)

        if proposicao_id:
            proposicao = buscar_proposicao(proposicao_id)

            if proposicao:
                fonte_id = proposicao["situacao_atual"].get("fonte")
                fonte = buscar_fonte(fonte_id) if fonte_id else None

                responder_tramitacao(proposicao, fonte)
                return

    print(f"\nIntenção identificada: {intencao}")

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