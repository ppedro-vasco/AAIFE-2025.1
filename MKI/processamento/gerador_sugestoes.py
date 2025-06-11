from typing import List
from modelos.videoDTO import Video


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

    sugestoes = []
    for video in base_simulada:
        if (
            video.category_id not in dominantes and
            video.video_id not in assistidos_ids
        ):
            sugestoes.append(video)

        if len(sugestoes) >= limite:
            break

    return sugestoes
