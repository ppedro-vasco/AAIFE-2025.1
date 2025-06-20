import os

class Config:
    """Configurações da aplicação Flask."""
    # Ativa o modo de depuração para obter mais informações de erro durante o desenvolvimento
    # Em produção, trocar para false.
    DEBUG = True

    # Chave secreta usada pelo Flask para seguraça
    SECRET_KEY = os.urandom(24)