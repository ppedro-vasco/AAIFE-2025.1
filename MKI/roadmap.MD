# 📌 Sistema de Recomendação Diversificada para Romper Bolhas Informacionais

Este projeto é um sistema experimental construído em Python que visa **identificar bolhas de filtro no consumo de vídeos** e **sugerir alternativas diversificadas** para ampliar a exposição informacional do usuário.

Inspirado no artigo *"A Conceptual Tool to Eliminate Filter Bubbles in Social Networks"* (Amrollahi, 2021), o sistema implementa os módulos `"Alert the Bubble"` e `"Burst the Bubble"` em ciclos progressivos.

---

## 🎯 Objetivo

Promover conscientização e diversidade informacional por meio de:
- Identificação de padrões de consumo concentrados (bolhas)
- Sugestões de vídeos de categorias e canais menos acessados
- Feedback claro, visual e explicativo

---

## 🧠 Base Conceitual

A bolha de filtro é uma condição em que o usuário é exposto a conteúdo repetitivo e semelhante, reforçado por algoritmos. O sistema baseia-se no modelo conceitual de Amrollahi (2021), com destaque para os seguintes componentes:

- **Alert**: Detecta a existência e intensidade da bolha com base em concentração temática, entropia e visualização.
- **Burst**: Sugere conteúdo alternativo para romper a repetição e diversificar a exposição.

---

## 🛠️ Tecnologias Utilizadas

- Linguagem: **Python 3.x**
- Execução via terminal (`argparse`)
- Estrutura modular (leitura, análise, sugestão, exportação, visualização)
- Visualizações com `matplotlib`
- Saídas explicativas em JSON
- Preparado para extensão com API do YouTube e interface web

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
```

### `base_simulada.json` – Base geral de vídeos
Usada para gerar sugestões com foco em categorias e canais **não dominantes**.

### `recomendacoes.json` – Saída do sistema
Contém sugestões finais com justificativas legíveis:
```json
[
  {
    "video_id": "s1",
    "title": "A origem do universo",
    "category": "Ciência e Tecnologia",
    "justificativa": "Este vídeo pertence à categoria 'Ciência e Tecnologia', que representa apenas 0.0% do seu histórico."
  }
]
```

---

## 🚀 Como Executar

```bash
python main.py --input=data/historico.json --output=data/recomendacoes.json
```

Parâmetros opcionais:
```bash
--threshold_individual=0.7
--threshold_soma_top_n=0.9
--n_top_categorias=2
--limite=10
```

---

## 📊 Funcionalidades Implementadas

### ✅ Módulo “Alert the Bubble”
- Agrupamento por categorias
- Identificação de dominância por threshold individual e top-N
- Cálculo de **entropia de Shannon** da distribuição
- Classificação da severidade da bolha (Alta, Média, Baixa)
- **Gráfico de pizza** para visualizar concentração
- Alerta textual exibido no terminal

### ✅ Módulo “Burst the Bubble”
- Sugestão de vídeos de categorias pouco acessadas
- **Filtragem por canais ainda não consumidos**
- **Ranqueamento por diversidade de canal**
- Exportação final com **justificativas** no JSON
- Sugestões explicadas no terminal, exemplo:

```text
📌 Sugestões com justificativas:

→ Melhores Gols da Semana (Esportes)
   Justificativa: Este vídeo pertence à categoria 'Esportes', que representa apenas 0.0% do seu histórico.

→ A Vida Secreta das Abelhas (Educação)
   Justificativa: Este vídeo pertence à categoria 'Educação', que representa apenas 10.0% do seu histórico.

→ Stand-up Show Incrível (Humor)
   Justificativa: Este vídeo pertence à categoria 'Humor', que representa apenas 0.0% do seu histórico.
```

---

## 🗺️ Roadmap por Marcos

| Marco | Entregável                                                             | Status       |
|-------|------------------------------------------------------------------------|--------------|
| M1    | MVP funcional: detecção básica de bolha e sugestões fora dela          | ✅ Concluído |
| M2    | Avaliação de intensidade da bolha + visualização gráfica               | ✅ Concluído |
| M3    | Justificativas nas sugestões + recomendação e ranqueamento por canais  | ✅ Concluído |
| M4    | Conexão com YouTube API + OAuth 2.0                                    | ⏳ Planejado |
| M5    | Interface gráfica/web interativa para alertas e sugestões              | ⏳ Planejado |

---

## 📚 Referência Teórica

Amrollahi, A. (2021). *A Conceptual Tool to Eliminate Filter Bubbles in Social Networks*.  
Proceedings of the 54th Hawaii International Conference on System Sciences.

---

## 📬 Contato

Este projeto faz parte de um Trabalho de Conclusão de Curso (TCC) em Sistemas de Informação.  
Para mais informações, entre em contato com:

- GitHub: [@ppedro-vasco](https://github.com/ppedro-vasco)
- E-mail: pedro.vasconcelos.2019003566@estudante.ifsudestemg.edu.br