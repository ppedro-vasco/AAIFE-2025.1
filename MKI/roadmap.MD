# 📌 Sistema de Recomendação Diversificada para Romper Bolhas Informacionais

Este projeto é um sistema experimental construído em Python que visa **identificar bolhas de filtro no consumo de vídeos** e **sugerir alternativas diversificadas** para ampliar a exposição informacional do usuário.

Inspirado no artigo *"A Conceptual Tool to Eliminate Filter Bubbles in Social Networks"* (Amrollahi, 2021), o sistema implementa os módulos `"Alert the Bubble"` e `"Burst the Bubble"` em ciclos progressivos.

---

## 🎯 Objetivo

Promover conscientização e diversidade informacional por meio de:
- Identificação de padrões de consumo concentrados (bolhas)
- Sugestões de vídeos de categorias menos acessadas
- Feedback claro, visual e, futuramente, contextual

---

## 🧠 Base Conceitual

A bolha de filtro é uma condição em que o usuário é exposto a conteúdo repetitivo e semelhante, reforçado por algoritmos. O sistema baseia-se no modelo conceitual de Amrollahi (2021), com destaque para os seguintes componentes:

- **Alert**: Detecta a existência e intensidade da bolha com base em concentração temática, entropia e visualização.
- **Burst**: Sugere conteúdo alternativo para romper a repetição e diversificar a exposição.

---

## 🛠️ Tecnologias Utilizadas

- Linguagem: **Python 3.x**
- Execução via terminal (`argparse`)
- Estrutura modular (módulos: leitura, análise, sugestão, exportação, visualização)
- Visualizações com `matplotlib`
- Saídas em JSON
- Pronto para extensão com API do YouTube e frontend

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
base_simulada.json – Base geral de vídeos
Usada para gerar sugestões com foco em categorias não dominantes.

recomendacoes.json – Saída do sistema
Contém sugestões finais formatadas para visualização ou consumo posterior:

json
Copiar
Editar
[
  {
    "video_id": "s1",
    "title": "Vídeo Y",
    "category": "Ciência e Tecnologia"
  }
]
🚀 Como Executar
bash
Copiar
Editar
python main.py --input=data/historico.json --output=data/recomendacoes.json
Parâmetros opcionais:

bash
Copiar
Editar
--threshold_individual=0.7
--threshold_soma_top_n=0.85
--n_top_categorias=2
--limite=5
📊 Funcionalidades Implementadas
✅ Módulo “Alert the Bubble”
Agrupamento por categorias

Identificação de dominância (threshold por categoria e top-N)

Cálculo de entropia de Shannon da distribuição de consumo

Classificação da severidade da bolha (Alta, Média, Baixa)

Exibição de gráfico de pizza da distribuição com matplotlib

✅ Módulo “Burst the Bubble”
Sugestão de vídeos de categorias pouco acessadas

Filtragem para evitar repetições do histórico

Exportação final em recomendacoes.json

🗺️ Roadmap por Marcos
Marco	Entregável	Status
M1	MVP funcional: detecção básica de bolha e sugestões fora dela	✅ Concluído
M2	Avaliação de intensidade da bolha + visualização gráfica	✅ Concluído
M3	Justificativas nas sugestões + recomendação de canais	⏳ Planejado
M4	Conexão com YouTube API + OAuth 2.0	⏳ Planejado
M5	Interface gráfica/web interativa para alertas e sugestões	⏳ Planejado

📚 Referência Teórica
Amrollahi, A. (2021). A Conceptual Tool to Eliminate Filter Bubbles in Social Networks.
Proceedings of the 54th Hawaii International Conference on System Sciences.

📬 Contato
Este projeto faz parte de um trabalho acadêmico de graduação em Sistemas de Informação.
Para mais informações, entre em contato com:

GitHub: @ppedro-vasco

E-mail: pedro.vasconcelos.2019003566@estudante.ifsudestemg.edu.br

yaml
Copiar
Editar

---

Você pode copiar esse conteúdo para um arquivo chamado `README.md` na raiz do seu projeto.  
Quer que eu gere esse arquivo `.md` diretamente e te envie?