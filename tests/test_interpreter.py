from src.interpreter import (
    identificar_intencao,
    identificar_proposicao,
    identificar_decisao,
)


def test_identifica_intencao_competencia():
    consulta = "quem cuida do policiamento nas ruas?"

    assert identificar_intencao(consulta) == "competencia"


def test_identifica_intencao_decisao():
    consulta = "o TSE decidiu sobre inelegibilidade por violência contra a mulher?"

    assert identificar_intencao(consulta) == "decisao"


def test_identifica_intencao_tramitacao():
    consulta = "o PLP 197/2024 já foi aprovado?"

    assert identificar_intencao(consulta) == "tramitacao"


def test_identifica_proposicao():
    consulta = "qual a situação do PLP 197/2024?"

    assert identificar_proposicao(consulta) == "plp_197_2024"

def test_identifica_decisao_tse():
    consulta = (
        "o TSE decidiu sobre inelegibilidade "
        "por violência contra a mulher?"
    )

    assert identificar_decisao(consulta) == "decisao_tse_2026_10_29"


def test_nao_identifica_decisao_com_termo_generico():
    consulta = "o TSE tomou uma decisão?"

    assert identificar_decisao(consulta) is None