def montar_contexto(pergunta, perfil, historico, produtos, conceitos, cenarios, transacoes):
    pergunta_lower = pergunta.lower()

    contexto = f"""
Usuário: {perfil.get('nome')}
Perfil: {perfil.get('perfil_investidor')} | Nível: {perfil.get('nivel_conhecimento')}
Objetivo: {perfil.get('objetivo_principal')}
"""

    # 🔹 CONCEITOS
    for termo, conteudo in conceitos.items():
        if termo in pergunta_lower:
            contexto += f"\nConceito ({termo}): {conteudo.get('explicacao')}"

    # 🔹 PRODUTOS
    for produto in produtos:
        nome = produto.get("nome", "").lower()
        if nome.split()[0] in pergunta_lower:
            contexto += f"""
            
Produto: {produto.get('nome')}
- Risco: {produto.get('risco')}
- Liquidez: {produto.get('liquidez')}
- Rentabilidade: {produto.get('rentabilidade')}
- Explicação: {produto.get('explicacao')}
"""

    # 🔹 HISTÓRICO (leve)
    try:
        ultimos = historico["tema"].tail(2).tolist()
        contexto += f"\nHistórico recente: {ultimos}"
    except:
        pass

    # 🔹 CENÁRIOS (apenas se relevante)
    if "juros" in pergunta_lower:
        for nome, cenario in cenarios.items():
            contexto += f"\nCenário ({nome}): {cenario.get('explicacao')}"

    return contexto