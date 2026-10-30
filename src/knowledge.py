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