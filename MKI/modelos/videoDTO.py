from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict


@dataclass
class Video:
    video_id: str
    title: str
    channel: str
    published_at: datetime
    category_id: int

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Video":
        try:
            return Video(
                video_id=str(data["video_id"]),
                title=str(data["title"]),
                channel=str(data["channel"]),
                published_at=datetime.fromisoformat(data["publishedAt"]),
                category_id=int(data["categoryId"]),
            )
        except (KeyError, ValueError, TypeError) as e:
            raise ValueError(f"Erro ao processar vídeo: {e}")