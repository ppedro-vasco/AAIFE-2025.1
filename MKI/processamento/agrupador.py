import math
from typing import List, Dict, Tuple
from collections import Counter
from modelos.videoDTO import Video

def agrupar_por_categoria(videos: List[Video]) -> Dict[int, int]:
    """
    Retorna um dicionário com contagem de vídeos por category_id.
    """
    categorias = [video.category_id for video in videos]

    return dict(Counter(categorias))

def calcular_entropia(distribuicao: Dict[int, int]) -> float:
    """
    Calcula a entropia de Shannon da distribuição de categorias.
    """
    total = sum(distribuicao.values())
    if total == 0:
        return 0.0
    
    entropia = 0.0
    for qtd in distribuicao.values():
        p = qtd / total
        if p > 0:
            entropia -= p * math.log2(p)
    
    return round(entropia, 4)

def classificar_intensidade_bolha(entropia: float) -> str:
    """
    Classifica a severidade da bolha com base na entropia.
    """
    if entropia < 1.0:
        return "Alta"
    elif entropia < 2.0:
        return "Média"
    else:
        return "Baixa"

def identificar_bolha_e_dominantes(
    agrupamento: Dict[int, int],
    total_videos: int,
    threshold_categoria_individual: float = 0.6,
    threshold_soma_categorias_top_n: float = 0.8,
    n_top_categorias: int = 3
) -> Tuple[List[int], bool, float, str]:
    """
    Identifica categorias dominantes e determina se o consumo forma uma bolha social
    com base na concentração de categorias.
    Inspirado no componente 'Alert' (identificação e avaliação) do artigo. 

    Args:
        agrupamento (Dict[int, int]): Dicionário com contagem de vídeos por category_id.
        total_videos (int): Número total de vídeos no histórico.
        threshold_categoria_individual (float): Limite percentual para uma categoria ser considerada dominante individualmente. 
        threshold_soma_categorias_top_n (float): Limite percentual para a soma das N categorias mais populares indicar uma bolha.
        n_top_categorias (int): Quantidade de categorias mais populares a considerar para o threshold_soma_categorias_top_n.

    Returns:
        Tuple[List[int], bool]: Uma tupla contendo a lista de categorias dominantes,
                                um booleano indicando se uma bolha foi identificada,
                                a entropia calculada e o nível de severidade da bolha.
    """
    if total_videos == 0:
        return [], False, 0.0, "Baixa"

    dominantes = []
    proporcoes = {}
    for categoria, quantidade in agrupamento.items():
        proporcao = quantidade / total_videos
        proporcoes[categoria] = proporcao
        if proporcao > threshold_categoria_individual:
            dominantes.append(categoria)

    # Ordenar categorias por proporção em ordem decrescente para analisar as top N
    categorias_ordenadas = sorted(proporcoes.items(), key=lambda item: item[1], reverse=True)

    soma_proporcoes_top_n = 0
    # Garante que não se tente acessar mais categorias do que existem
    n_top_considerar = min(n_top_categorias, len(categorias_ordenadas))
    for i in range(n_top_considerar):
        soma_proporcoes_top_n += categorias_ordenadas[i][1]

    #Calcular Entropia e Severidade
    entropia_calculada = calcular_entropia(agrupamento)
    severidade_calculada = classificar_intensidade_bolha(entropia_calculada)

    bolha_identificada = False
    # Uma bolha é identificada se a soma das top N categorias excede o threshold
    if soma_proporcoes_top_n > threshold_soma_categorias_top_n:
        bolha_identificada = True
    # Ou se houver pelo menos uma categoria individualmente dominante (conforme critério anterior)
    if dominantes:
        bolha_identificada = True 
    # Se a severidade da bolha (pela entropia) não for "Baixa", considere uma bolha.
    if severidade_calculada in ["Alta", "Média"]:
        bolha_identificada = True

    return dominantes, bolha_identificada, entropia_calculada, severidade_calculada

def analisar_categorias(
    videos: List[Video],
    threshold_categoria_individual: float = 0.6,
    threshold_soma_categorias_top_n: float = 0.8,
    n_top_categorias: int = 3
) -> Tuple[Dict[int, int], List[int], bool, float, str]:
    """
    Função de alto nível: retorna o agrupamento, as categorias dominantes,
    indica se uma bolha social foi identificada, a entropia e o nível de severidade.
    """
    agrupamento = agrupar_por_categoria(videos)
    dominantes, bolha_identificada, entropia, severidade = identificar_bolha_e_dominantes(
        agrupamento,
        len(videos),
        threshold_categoria_individual,
        threshold_soma_categorias_top_n,
        n_top_categorias
    )

    return agrupamento, dominantes, bolha_identificada, entropia, severidade