#interpretar a pergunta

def buscar_competencia(consulta, competencias):
    consulta = consulta.lower().strip()

    for competencia in competencias:
        assunto = competencia["assunto"].replace("_", " ")

        if assunto in consulta:
            return competencia

        for termo in competencia.get("termos", []):
            if termo.lower() in consulta:
                return competencia

    return None


def identificar_tema(consulta, tema):
    consulta = consulta.lower().strip()

    for termo in tema.get("termos", []):
        if termo.lower() in consulta:
            return True

    return False

def identificar_intencao(consulta):
    consulta = consulta.lower().strip()

    termos_tramitacao = [
        "tramitação",
        "tramita",
        "situação",
        "status",
        "aprovado",
        "relator",
        "congresso"
    ]

    termos_decisao = [
        "tse",
        "decisão",
        "decidiu",
        "julgamento",
        "inelegibilidade"
    ]

    for termo in termos_tramitacao:
        if termo in consulta:
            return "tramitacao"

    for termo in termos_decisao:
        if termo in consulta:
            return "decisao"

    return "competencia"

def identificar_proposicao(consulta):
    consulta = consulta.lower()

    if "plp 197/2024" in consulta:
        return "plp_197_2024"

    if "plp 197" in consulta:
        return "plp_197_2024"

    return None