# backend/src/routes/analysis_routes.py

from flask import Blueprint, request, jsonify
from ..services.bubble_service import BubbleService
from ..utils import json_handler
import os

analysis_bp = Blueprint('analysis_bp', __name__)
bubble_service = BubbleService()

SUGGESTION_POOL_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'base_simulada.json')


@analysis_bp.route('/analyze', methods=['POST'])
def analyze_history():
    if 'history_file' not in request.files:
        return jsonify({"error": "Nenhum arquivo de histórico foi enviado."}), 400

    history_file = request.files['history_file']
    if history_file.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado."}), 400

    try:
        history_videos = json_handler.load_videos_from_stream(history_file.stream)
        if not history_videos:
            return jsonify({"error": "O arquivo de histórico está vazio ou é inválido."}), 400

        # Garantir que o arquivo da base de sugestões existe
        if not os.path.exists(SUGGESTION_POOL_PATH):
            return jsonify({"error": f"Arquivo de sugestões não encontrado em {SUGGESTION_POOL_PATH}"}), 500

        with open(SUGGESTION_POOL_PATH, 'r', encoding='utf-8') as f:
            suggestion_pool_videos = json_handler.load_videos_from_stream(f)

    except Exception as e:
        return jsonify({"error": f"Falha ao processar os arquivos: {str(e)}"}), 500

    final_report = bubble_service.run_full_analysis(history_videos, suggestion_pool_videos)

    return jsonify(final_report), 200