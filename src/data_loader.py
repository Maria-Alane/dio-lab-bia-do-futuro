import pandas as pd
import json
import os

def carregar_dados():
    base_path = os.path.dirname(__file__)

    # CSV
    historico = pd.read_csv(os.path.join(base_path, '../data/historico_investimentos.csv'))
    transacoes = pd.read_csv(os.path.join(base_path, '../data/transacoes.csv'))

    # JSON
    with open(os.path.join(base_path, '../data/perfil_investidor.json'), 'r', encoding='utf-8') as f:
        perfil = json.load(f)

    with open(os.path.join(base_path, '../data/produtos_investimentos.json'), 'r', encoding='utf-8') as f:
        produtos = json.load(f)

    with open(os.path.join(base_path, '../data/conceitos.json'), 'r', encoding='utf-8') as f:
        conceitos = json.load(f)

    with open(os.path.join(base_path, '../data/cenarios_mercados.json'), 'r', encoding='utf-8') as f:
        cenarios = json.load(f)

    return historico, transacoes, perfil, produtos, conceitos, cenarios