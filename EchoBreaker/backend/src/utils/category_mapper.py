# backend/src/utils/category_mapper.py

from typing import List, Dict

CATEGORYS: Dict[int, str] = {
    1: "Filme e Animação",
    2: "Automóveis e Veículos",
    10: "Música",
    15: "Animais de Estimação",
    17: "Esportes",
    19: "Viagens e Eventos",
    20: "Games",
    22: "Pessoas e Blogs",
    23: "Comédia",
    24: "Entretenimento",
    25: "Notícias e Política",
    26: "Como fazer e Estilo",
    27: "Educação",
    28: "Ciência e Tecnologia",
    29: "ONGs e Ativismo"
}

def get_category_name(category_id) -> str:
    """Retorna o nome de uma categoria a partir de seu ID."""
    return CATEGORYS.get(category_id, "Desconhecida")

def get_all_categorys() -> List[int]:
    """Retorna uma lista de categorias com ID's conhecidos"""
    return list(CATEGORYS.keys())