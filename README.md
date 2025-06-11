# Algoritmo para Diversificação de Conteúdo nas Redes Sociais

## Visão Geral do Projeto

Este projeto desenvolve um algoritmo em Python focado na diversificação do consumo de conteúdo de vídeos em redes sociais, especificamente o YouTube, para mitigar a formação das chamadas "bolhas sociais" ou "algorítmicas". O sistema analisa o histórico de vídeos assistidos por um usuário, identifica padrões de consumo por categoria e sugere novos vídeos de categorias pouco ou nunca exploradas. [cite_start]O objetivo é expandir as perspectivas do usuário, combatendo a polarização e a exposição limitada a diferentes tipos de informação.

[cite_start]A dependência do uso massivo de redes sociais como fonte primária de informação levanta desafios significativos, como a limitação das fontes às preferências dos usuários. [cite_start]A formação dessas bolhas de filtro é reconhecida como um risco à democracia, podendo levar à polarização da sociedade, tendências a pontos de vista extremistas e à proliferação de notícias falsas. [cite_start]Nosso algoritmo busca, portanto, "alertar" o usuário sobre a possível existência de uma bolha em seu consumo e ativamente "estourar" essa bolha através da diversificação de conteúdo sugerido.

## Requisitos Funcionais (MVP)

A versão atual (MVP - Produto Mínimo Viável) do sistema foca nos seguintes requisitos funcionais:

* **RF01 – Autenticação do Usuário na API do YouTube:** O sistema permite a autenticação da conta Google do usuário para acesso ao seu histórico público. [cite_start]No MVP, utiliza-se um arquivo JSON contendo uma simulação do histórico de vídeos para simplificar.
* [cite_start]**RF02 – Coleta de Vídeos Consumidos:** O sistema extrai informações sobre os vídeos assistidos recentemente, incluindo `video_id`, `title`, `channel`, `publishedAt`, e `categoryId`.
* **RF03 – Agrupamento por Categorias:** Os vídeos consumidos são agrupados com base em seus `categoryId`s. O sistema identifica categorias dominantes, que são aquelas com mais de um determinado percentual de presença no histórico do usuário. A detecção de uma "bolha" ocorre se uma única categoria excede um threshold ou se um conjunto de categorias mais populares excede outro threshold de concentração.
* **RF04 – Geração de Sugestões Diversificadas:** O sistema retorna uma lista de vídeos provenientes de categorias pouco ou nunca acessadas pelo usuário. [cite_start]Para o MVP, os vídeos sugeridos são populares ou recentes nessas categorias (simulados).
* [cite_start]**RF05 – Exportação de Sugestões em JSON:** As sugestões geradas são salvas em um arquivo `recomendacoes.json` com o formato `[{"video_id": "...", "title": "...", "category": "..."}]`.
* [cite_start]**RF06 – Interface de Linha de Comando:** O MVP é executado via terminal, utilizando argumentos para entrada e saída de dados.

## Requisitos Não-Funcionais

* [cite_start]**NFR01:** O sistema funciona offline após a obtenção inicial dos dados, sem a necessidade de chamadas adicionais à API.
* [cite_start]**NFR02:** A execução completa do sistema não deve exceder 15 segundos para um histórico de até 100 vídeos.
* [cite_start]**NFR03:** O sistema possui uma arquitetura modularizada, com separação clara entre os módulos de leitura de dados, análise/geração de sugestões e exportação JSON.

## Tecnologias Envolvidas (MVP)

* [cite_start]**Linguagem:** Python 3.x 
* **Bibliotecas Principais:**
    * [cite_start]`google-api-python-client` (para futura integração com a API do YouTube) 
    * [cite_start]`pandas` (para manipulação e processamento de dados) 
    * [cite_start]`collections` (para contagem e agrupamento eficiente) 
    * [cite_start]`datetime`, `typing` (para suporte a tipos e manipulação de datas) 
* [cite_start]**Formato de Saída:** Arquivo JSON 

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado. As bibliotecas necessárias podem ser instaladas via `pip`:

```bash
pip install pandas google-api-python-client
