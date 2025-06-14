import json
from typing import List, Dict
from modelos.videoDTO import Video
from utils.categorias import mapear_categoria


def exportar_sugestoes_json(
        sugestoes: List[Video], 
        caminho_saida: str, 
        historico: List[Video]
        ) -> None:
    """
    Exporta sugestões em JSON, com campo 'justificativa' baseado na sub-representação da categoria.
    """
    total = len (historico)
    categoria_freq: Dict[int, int] = {}
    for video in historico:
        categoria_freq[video.category_id] = categoria_freq.get(video.category_id, 0) + 1
    
    json_saida = []
    for video in sugestoes:
        categoria_nome = mapear_categoria(video.category_id)
        frequencia = categoria_freq.get(video.category_id, 0)
        percentual = (frequencia/total) * 100 if total > 0 else 0.0

        justifica = (
            f"Este vídeo pertence à categoria '{categoria_nome}', "
            f"que representa apenas {percentual: .1f}% do seu histórico."
        )
        
        json_saida.append({
            "video_id": video.video_id,
            "title": video.title,
            "category": categoria_nome,
            "justificativa": justifica
        })

    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(json_saida, f, ensure_ascii=False, indent=2)
