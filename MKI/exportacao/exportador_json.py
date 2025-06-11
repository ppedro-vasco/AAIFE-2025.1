import json
from typing import List
from modelos.videoDTO import Video
from utils.categorias import mapear_categoria


def exportar_sugestoes_json(videos: List[Video], caminho_saida: str) -> None:
    sugestoes = []
    for video in videos:
        sugestoes.append({
            "video_id": video.video_id,
            "title": video.title,
            "category": mapear_categoria(video.category_id)
        })

    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(sugestoes, f, ensure_ascii=False, indent=2)
