# 📌 Sistema de Recomendação Diversificada para Romper Bolhas Informacionais

Este projeto é um sistema experimental construído em Python que visa **identificar bolhas de filtro no consumo de vídeos** e **sugerir alternativas diversificadas** para ampliar a exposição informacional do usuário.

Inspirado no artigo *"A Conceptual Tool to Eliminate Filter Bubbles in Social Networks"* (Amrollahi, 2021), o sistema implementa os módulos "Alert the Bubble" e "Burst the Bubble" em ciclos progressivos.

---

## 🎯 Objetivo

Promover conscientização e diversidade informacional por meio de:
- Identificação de padrões de consumo concentrados (bolhas)
- Sugestões de vídeos de categorias menos acessadas
- Feedback claro e, futuramente, visual e contextual

---

## 🧠 Base Conceitual

A bolha de filtro é uma condição em que o usuário é exposto a conteúdo repetitivo e semelhante, reforçado por algoritmos. O sistema baseia-se no modelo conceitual de Amrollahi (2021), com destaque para os seguintes componentes:

- **Alert**: Detecta a existência e intensidade da bolha com base em concentração temática
- **Burst**: Sugere conteúdo alternativo para romper a repetição e diversificar a exposição

---

## 🛠️ Tecnologias Utilizadas

- Linguagem: **Python 3.x**
- Execução via terminal (`argparse`)
- Estrutura modular (módulos: leitura, análise, sugestão, exportação)
- Saídas em JSON
- Extensões planejadas com visualização (`matplotlib`) e integração com a API do YouTube

---

## 📁 Estrutura de Dados

### `historico.json` – Vídeos já assistidos
```json
[
  {
    "video_id": "v1",
    "title": "Vídeo X",
    "channel": "Canal X",
    "publishedAt": "2024-01-01T00:00:00",
    "categoryId": 24
  }
]

🗺️ Roadmap por Marcos
Marco   Entregável	                                                    Status
M1	    MVP funcional: detecção básica de bolha e sugestões fora dela	✅ Concluído
M2	    Avaliação de intensidade da bolha + visualização gráfica	    🔄 Em andamento
M3	    Justificativas nas sugestões + recomendação de canais	        ⏳ Planejado
M4	    Conexão com YouTube API + OAuth 2.0	                            ⏳ Planejado
M5	    Interface gráfica/web interativa para alertas e sugestões	    ⏳ Planejado

📚 Referência Teórica
Amrollahi, A. (2021). A Conceptual Tool to Eliminate Filter Bubbles in Social Networks. Proceedings of the 54th Hawaii International Conference on System Sciences.

📬 Contato
Este projeto faz parte de um trabalho acadêmico de graduação em Sistemas de Informação. Para mais informações, entre em contato com:
{
    @ppedro-vasco
    pedro.vasconcelos.2019003566@estudante.ifsudestemg.edu.br.
}
