from typing import List
from modelos.videoDTO import Video
from collections import Counter


def gerar_sugestoes_diversificadas(
    historico: List[Video],
    dominantes: List[int],
    base_simulada: List[Video],
    limite: int = 10
) -> List[Video]:
    """
    Retorna sugestões de vídeos de categorias não-dominantes e não assistidos.
    """
    assistidos_ids = {video.video_id for video in historico}
    canais_assistidos = {video.channel for video in historico}
    canais_frequencia = Counter(canais_assistidos)

    candidatos = [
        video for video in base_simulada
        if video.video_id not in assistidos_ids
        and video.category_id not in dominantes
    ]

    # Ordena por frequência crescente do canal (menos visto primeiro)
    candidatos.sort(key=lambda v: canais_frequencia.get(v.channel, 0))

    return candidatos[:limite]