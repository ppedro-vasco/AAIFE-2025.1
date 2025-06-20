# backend/src/utils/json_handler.py

import json
from typing import List, Dict, Any
from ..models.video import Video

def load_videos_from_stream(file_stream) -> List[Video]:
    """
    Carrega e processa uma lista de vídeos a partir de um stream de arquivo JSON
    (como um arquivo enviado via formulário web).

    Args:
        file_stream: O objeto de arquivo aberto para leitura.

    Returns:
        Uma lista de objetos Video. Retorna lista vazia se houver erro.
    """
    try:
        # Carrega os dados do stream do arquivo
        data = json.load(file_stream)

        if not isinstance(data, list):
            print("Aviso: O JSON n'ao contém uma lista de vídeos.")
            return []
        
        videos = []
        for item in data:
            # Utilizando um factory method do modelo Video
            video = Video.from_dict(item)
            # Adiciona à lista apenas se o vídeo for processado com sucesso
            if video:
                videos.append(video)
        
        return videos
    
    except json.JSONDecodeError:
        print("Erro: O arquivo fornecido não é um JSON válido.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar o arquivo: {e}")
        return []