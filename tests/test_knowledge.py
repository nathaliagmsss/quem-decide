from src.knowledge import (
    buscar_proposicao,
    buscar_fonte,
    buscar_decisao,
)

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

def test_buscar_decisao_tse():
    decisao = buscar_decisao("decisao_tse_2026_10_29")

    assert decisao is not None
    assert decisao["sigla_orgao"] == "TSE"
    assert decisao["cria_nova_hipotese_legal"] is False