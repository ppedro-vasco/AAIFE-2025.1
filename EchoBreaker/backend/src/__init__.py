# backend/src/__init__.py

from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.analysis_routes import analysis_bp

# Instancia principal do Flask
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# --- Registro de Rotas (Blueprints) ---
app.register_blueprint(analysis_bp, url_prefix='/api')

# --- Rota de Teste ---
@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return {"message": "pong!"}