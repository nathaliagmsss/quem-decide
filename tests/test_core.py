from src.core import processar_pergunta


def test_processa_pergunta_sobre_tramitacao():
    resposta = processar_pergunta(
        "o PLP 197/2024 já foi aprovado?"
    )

    assert resposta is not None
    assert resposta["tipo"] == "tramitacao"
    assert resposta["proposicao"]["numero"] == "197/2024"
    assert resposta["fonte"] is not None


def test_processa_pergunta_sobre_decisao():
    resposta = processar_pergunta(
        "o TSE decidiu sobre inelegibilidade "
        "por violência contra a mulher?"
    )

    assert resposta is not None
    assert resposta["tipo"] == "decisao"
    assert resposta["decisao"]["sigla_orgao"] == "TSE"
    assert resposta["fonte"] is not None


def test_core_nao_inventa_resposta():
    resposta = processar_pergunta(
        "qual é a situação do PLP 999/2099?"
    )

    assert resposta is None

def test_processa_pergunta_sobre_competencia():
    resposta = processar_pergunta(
        "quem cuida do policiamento nas ruas?"
    )

    assert resposta is not None
    assert resposta["tipo"] == "competencia"
    assert resposta["competencia"]["orgao"] == "Polícia Militar"
    assert resposta["competencia"]["ente"] == "Estado"


def test_core_detecta_tema_ambiguo():
    resposta = processar_pergunta(
        "quem é responsável pela segurança pública?"
    )

    assert resposta is not None
    assert resposta["tipo"] == "tema_ambiguo"
    assert resposta["tema"]["nome"] == "Segurança Pública"


def test_core_nao_responde_assunto_fora_da_base():
    resposta = processar_pergunta(
        "quem é responsável pela merenda escolar?"
    )

    assert resposta is None