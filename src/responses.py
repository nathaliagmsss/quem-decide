def responder_tramitacao(proposicao, fonte=None):
    situacao = proposicao["situacao_atual"]
    status = situacao["status"]

    print("\n--- Quem Decide? ---")

    if status == "aguardando_designacao_de_relator":
        print(
            f"Não. O {proposicao['tipo']} {proposicao['numero']} "
            "ainda não foi aprovado."
        )

    print(
        f"\nNa última consulta registrada ({situacao['data_consulta']}), "
        f"a proposição estava na {situacao['sigla_orgao']} "
        f"({situacao['orgao']}), "
        f"com status: {status.replace('_', ' ')}."
    )
    if fonte:
        print("\nFonte oficial:")
        print(f"{fonte['instituicao']} — {fonte['titulo']}")
        print(fonte["url"])