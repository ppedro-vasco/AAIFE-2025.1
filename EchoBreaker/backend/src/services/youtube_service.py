# backend/src/services/youtube_service.py

import yt_dlp
from typing import Dict, List, Any

class YouTubeService:
    """Serviço que interage com Youtube via yt-dlp"""

    def __init__(self):
        self.ydl_opts = {
            'skip_download': True,
            'quiet': True,
            'force_generic_extractor': True,
            'noplaylist': True,
            'no_warnings': True,
            'cachedir': False,
        }

    def fetch_metadata_for_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        """
        Busca metadados para uma lista de URLs.
        Retorna uma lista de dicionários com os dados brutos do yt-dlp.
        """
        all_metadata = []
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            for url in urls:
                try:
                    info_dict = ydl.extract_info(url, download=False)
                    if info_dict:
                        # Em caso de playlists, pega o primeiro vídeo
                        video_data = info_dict['entries'][0] if 'entries' in info_dict else info_dict
                        all_metadata.append(video_data)
                except Exception as e:
                    print(f"Aviso: Falha ao buscar metadados para a URL {url}: {e}")
        return all_metadata