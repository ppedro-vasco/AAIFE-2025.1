import json
from typing import List
from modelos.videoDTO import Video


def carregar_historico(path: str) -> List[Video]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
            
        videos = []
        for item in dados:
            try:
                video = Video.from_dict(item)
                videos.append(video)
            except ValueError as e:
                print(f"[AVISO] Vídeo ignorado por erro: {e}")
        return videos

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{path}' não encontrado.")
    except json.JSONDecodeError:
        raise ValueError(f"Arquivo '{path}' não é um JSON válido.")