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

def responder_decisao(decisao, fonte=None):
    print("\n--- Quem Decide? ---")

    print(
        f"Sim. Em {decisao['data']}, o {decisao['sigla_orgao']} "
        "analisou um caso envolvendo inelegibilidade por condenação "
        "criminal relacionada à violência contra a mulher."
    )

    if decisao["cria_nova_hipotese_legal"] is False:
        print(
            "\nA decisão não criou uma nova hipótese legal de "
            "inelegibilidade. O tribunal interpretou e aplicou "
            "uma norma já existente."
        )

    print(f"\nEfeito: {decisao['efeito']['descricao']}.")

    if fonte:
        print("\nFonte oficial:")
        print(f"{fonte['instituicao']} — {fonte['titulo']}")
        print(fonte["url"])