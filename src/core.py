from src.interpreter import (
    identificar_intencao,
    identificar_proposicao,
    identificar_decisao,
    buscar_competencia,
    identificar_tema,
)

from src.knowledge import (
    buscar_proposicao,
    buscar_decisao,
    buscar_fonte,
    carregar_competencias,
)


def processar_pergunta(pergunta):
    intencao = identificar_intencao(pergunta)

    if intencao == "tramitacao":
        return processar_tramitacao(pergunta)

    if intencao == "decisao":
        return processar_decisao(pergunta)

    if intencao == "competencia":
        return processar_competencia(pergunta)

    return None

def processar_competencia(pergunta):
    dados = carregar_competencias()

    competencias = dados["competencias"]
    tema = dados["tema"]

    competencia = buscar_competencia(
        pergunta,
        competencias,
    )

    if competencia:
        return {
            "tipo": "competencia",
            "competencia": competencia,
        }

    if identificar_tema(pergunta, tema):
        return {
            "tipo": "tema_ambiguo",
            "tema": tema,
            "competencias": competencias,
        }

    return None


def processar_tramitacao(pergunta):
    proposicao_id = identificar_proposicao(pergunta)

    if not proposicao_id:
        return None

    proposicao = buscar_proposicao(proposicao_id)

    if not proposicao:
        return None

    situacao = proposicao["situacao_atual"]

    fonte_id = situacao.get("fonte")
    fonte = buscar_fonte(fonte_id) if fonte_id else None

    return {
        "tipo": "tramitacao",
        "proposicao": proposicao,
        "situacao": situacao,
        "fonte": fonte,
    }


def processar_decisao(pergunta):
    decisao_id = identificar_decisao(pergunta)

    if not decisao_id:
        return None

    decisao = buscar_decisao(decisao_id)

    if not decisao:
        return None

    fonte_id = decisao.get("fontes", [None])[0]
    fonte = buscar_fonte(fonte_id) if fonte_id else None

    return {
        "tipo": "decisao",
        "decisao": decisao,
        "fonte": fonte,
    }