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