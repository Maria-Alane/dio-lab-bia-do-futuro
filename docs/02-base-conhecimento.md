# Base de Conhecimento

## Dados Utilizados

O agente utiliza diferentes arquivos da pasta data para enriquecer o contexto e tornar as respostas mais precisas e personalizadas.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `produtos_investimentos.json` | JSON | Explicar produtos financeiros reais (CDB, Tesouro Selic, etc.) |
| `conceitos.json` | JSON | Responder conceitos financeiros (risco, liquidez, diversificação, etc.) |
| `historico_investimentos.csv` | CSV | Identificar interesses recentes do usuário |
| `historico_atendimento.csv` | CSV | (Opcional) Histórico mais amplo de interações |
| `perfil_investidor.json` | JSON | Personalizar respostas com base no perfil do usuário (nome, renda, objetivo, nível) |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | (Preparado para uso) Analisar comportamento financeiro |

O projeto foi estruturado para ser escalável. Mesmo que nem todos os dados sejam usados diretamente no prompt atual, eles já estão organizados para futuras melhorias do agente.

---

## Adaptações nos Dados

Os dados foram ajustados para simular um cenário realista de um usuário iniciante em investimentos.

Principais adaptações:

- Criação de um perfil completo do investidor (`perfil_investidor.json`)
- Estruturação de produtos financeiros com:
   - risco
   - liquidez
   - rentabilidade
   -  explicação
   -ponto de atenção
- Criação de conceitos com:
   - explicação
   - analogia (para facilitar entendimento)
   - relação com outros conceitos
- Inclusão de históricos para simular contexto contínuo de atendimento
- Padronização dos dados para fácil leitura pelo agente

---

## Estratégia de Integração

### Como os dados são carregados?

Os dados são carregados no início da aplicação através da função:

`carregar_dados()`

Essa função:

-Lê arquivos JSON e CSV da pasta data

-Converte CSV em DataFrame (pandas)

-Retorna todos os dados já prontos para uso no app


### Como os dados são usados no prompt?

Os dados não são enviados completamente para o modelo.

Eles são utilizados de forma dinâmica e controlada, através do context_builder, que:

- Filtra apenas o que é relevante para a pergunta
- Evita excesso de informação
- Reduz alucinações

Exemplos de uso:

Se o usuário pergunta "O que é risco?"
 → busca em `conceitos.json`
 
Se pergunta "O que é CDB?"
 → busca em `produtos_investimentos.json`
 
Se pergunta sobre perfil
 → usa `perfil_investidor.json`


## Exemplo de Contexto Montado

Exemplo real do contexto enviado ao modelo:

```
PERFIL DO USUÁRIO:
Nome: Maria Silva
Perfil: moderado
Nível: iniciante
Objetivo: Construir reserva de emergência

CONCEITO:
Risco:
Explicação: Possibilidade de perdas ou variações no valor de um investimento.
Analogia: Como dirigir em alta velocidade: pode chegar mais rápido, mas com mais risco.
Relação: Maior risco geralmente está associado a maior potencial de retorno.
```

## Observações Importantes
- O agente não usa internet → apenas dados internos
- O agente não inventa produtos
- O agente não faz recomendações diretas
- O foco é educação financeira
