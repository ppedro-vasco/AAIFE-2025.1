# backend/src/models/video.py

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any, Dict
# Importamos nosso mapeador de categorias
from ..utils.category_mapper import get_category_name


@dataclass
class Video:
    """Representa a estrutura de dados para um único vídeo."""
    video_id: str
    title: str
    channel: str
    published_at: datetime
    category_id: int
    category_name: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Video":
        """
        Cria uma instância de Video a partir de um dicionário (do historico.json).
        """
        try:
            # CORREÇÃO 1: Usar a chave 'publishedAt' do seu JSON e o formato ISO.
            published_at_str = data["publishedAt"]
            # O 'Z' no final (Zulu time) pode não ser entendido por todas as versões do Python.
            # É mais seguro removê-lo antes de converter.
            if published_at_str.endswith('Z'):
                published_at_str = published_at_str[:-1]
            published_at_dt = datetime.fromisoformat(published_at_str)

            # CORREÇÃO 2: Usar a chave 'categoryId' do seu JSON.
            category_id = int(data["categoryId"])
            
            return Video(
                video_id=str(data["video_id"]),
                title=str(data["title"]),
                channel=str(data["channel"]),
                published_at=published_at_dt,
                category_id=category_id,
                category_name=get_category_name(category_id)
            )
        except (KeyError, ValueError, TypeError) as e:
            print(f"Aviso: Erro ao processar o vídeo {data.get('video_id', '')}. Chave ou formato inválido. Erro: {e}")
            return None

    def to_dict(self) -> Dict[str, Any]:
        """Converte a instância de Video para um dicionário serializável em JSON."""
        video_dict = asdict(self)
        video_dict['published_at'] = self.published_at.isoformat()
        return video_dict