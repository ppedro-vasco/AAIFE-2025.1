# backend/src/services/bubble_service.py

import math
from collections import Counter
from typing import List, Dict, Any, Tuple
from ..models.video import Video
from ..utils.category_mapper import get_category_name

class BubbleService:
    """Serviço com a lógica de negócio para análise de bolha e sugestões"""

    def _calculate_entropy(self, distribution: Dict[int, int]) -> float:
        """Cálculo da entropia de Shannon da distribuição de categorias."""

        total = sum(distribution.values())
        if total == 0:
            return 0.0
        entropy = 0.0
        for quantity in distribution.values():
            p = quantity / total
            if p > 0:
                entropy -= p * math.log2(p)
        return round(entropy, 4)
    
    def _analyze_bubble(self, history: List[Video]) -> Dict[str, Any]:
        """Analise do histórico para identificar a bolha social."""
        if not history:
            return {
                "is_bubble": False,
                "severity": "Baixa",
                "dominat_categories": [],
                "entropy": 0.0,
                "category_distribution": {},
            }
        total_videos = len(history)
        category_counts = Counter(video.category_id for video in history)

        # Identifica dominantes
        dominant_ids = [
            cat_id for cat_id, count in category_counts.items()
            if (count / total_videos) > 0.5 # Limar de 50% para ser dominante
        ]

        # Calcular Entropia e Severidade da bolha
        entropy = self._calculate_entropy(category_counts)
        severity = "Alta" if entropy < 1.5 else "Média" if entropy < 2.5 else "Baixa"
        is_bubble = severity in ["Alta", "Média"]

        # Formatar a distribuição para o relatório final
        category_distribution = {
            get_category_name(cat_id): count 
            for cat_id, count in category_counts.items()
        }

        return {
            "is_bubble": is_bubble,
            "severity": severity,
            "dominant_category_ids": dominant_ids,
            "entropy": entropy,
            "category_distribution": category_distribution
        }
    
    def _generate_suggestions(self, history: List[Video], analysis_results: Dict[str, Any], suggestion_pool: List[Video]) -> List[Dict[str, Any]]:
        """Gera e formata sugestões de vídeos diversificados."""
        history_ids = {video.video_id for video in history}
        dominant_ids = analysis_results["dominant_category_ids"]

        candidates = [
            video for video in suggestion_pool
            if video.video_id not in history_ids and video.category_id not in dominant_ids
        ]

        # Ordenar por canais menos vistos no histórico
        history_channel_freq = Counter(video.channel for video in history)
        candidates.sort(key=lambda v: history_channel_freq.get(v.channel, 0))

        # Formatar saída e criar justificativa
        formatted_suggestions = []
        history_category_counts = Counter(v.category_id for v in history)
        total_history_videos = len(history)

        for video in candidates [:10]: # Limita em 10 sugestões
            cat_name = get_category_name(video.category_id)
            cat_freq = history_category_counts.get(video.category_id, 0)
            percentage = (cat_freq / total_history_videos) * 100 if total_history_videos > 0 else 0

            justification = f"'{cat_name}' representa apenas {percentage:.1f}% do seu histórico."
            if percentage == 0:
                justification = f"A categoria '{cat_name}' não foi encontrada no seu histórico recente."

                formatted_suggestions.append({
                    "video_id": video.video_id,
                    "title": video.title,
                    "channel": video.channel,
                    "category": cat_name,
                    "justification": justification                    
                })

        return formatted_suggestions

    def run_full_analysis(self, history_videos: List[Video], suggestion_pool_videos: List[Video]) -> Dict[str, Any]:
        """Orquestra a análise completa e a geração de sugestões."""
        analysis_results = self._analyze_bubble(history_videos)
        suggestions = self._generate_suggestions(history_videos, analysis_results, suggestion_pool_videos)

        # Monta o objeto final de response da API
        final_report = {
            "analysis": analysis_results,
            "suggestions": suggestions
        }

        return final_report
