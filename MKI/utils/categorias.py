def mapear_categoria(category_id: int) -> str:
    categorias = {
        1: "Filme",
        2: "Automóveis",
        10: "Música",
        15: "Animais",
        17: "Esportes",
        20: "Jogos",
        22: "Pessoas e Blogs",
        23: "Humor",
        24: "Entretenimento",
        25: "Notícias",
        26: "Como fazer e Estilo",
        27: "Educação",
        28: "Ciência e Tecnologia",
        29: "ONGs e Ativismo"
    }
    return categorias.get(category_id, "Categoria desconhecida")
