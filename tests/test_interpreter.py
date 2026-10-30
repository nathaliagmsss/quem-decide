from src.interpreter import (
    identificar_intencao,
    identificar_proposicao,
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