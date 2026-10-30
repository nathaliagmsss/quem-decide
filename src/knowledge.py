import json
from pathlib import Path

#buscar/carregar conhecimento

BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "data" / "knowledge"


def carregar_json(nome_arquivo):
    caminho = KNOWLEDGE_DIR / nome_arquivo

    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)


def carregar_competencias():
    return carregar_json("competencias.json")

def carregar_base_conhecimento():
    base = []

    for caminho in KNOWLEDGE_DIR.glob("*.json"):
        with open(caminho, encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        base.append({
            "arquivo": caminho.name,
            "dados": dados
        })

    return base

def carregar_caso_002():
    return carregar_json("caso_002.json")


def buscar_proposicao(identificador):
    dados = carregar_caso_002()

    for proposicao in dados.get("proposicoes_legislativas", []):
        if proposicao["id"] == identificador:
            return proposicao

    return None

def buscar_fonte(fonte_id):
    dados = carregar_caso_002()

    for fonte in dados.get("fontes", []):
        if fonte["id"] == fonte_id:
            return fonte

    return None