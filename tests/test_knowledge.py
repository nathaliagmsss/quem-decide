from src.knowledge import buscar_proposicao, buscar_fonte


def test_buscar_proposicao_existente():
    proposicao = buscar_proposicao("plp_197_2024")

    assert proposicao is not None
    assert proposicao["numero"] == "197/2024"


def test_proposicao_possui_situacao_atual():
    proposicao = buscar_proposicao("plp_197_2024")

    assert "situacao_atual" in proposicao
    assert proposicao["situacao_atual"]["status"] == "aguardando_designacao_de_relator"


def test_situacao_atual_possui_fonte():
    proposicao = buscar_proposicao("plp_197_2024")

    fonte_id = proposicao["situacao_atual"]["fonte"]

    assert fonte_id is not None


def test_fonte_pode_ser_resolvida():
    proposicao = buscar_proposicao("plp_197_2024")
    fonte_id = proposicao["situacao_atual"]["fonte"]

    fonte = buscar_fonte(fonte_id)

    assert fonte is not None
    assert fonte["instituicao"] == "Senado Federal"
    assert fonte["url"]