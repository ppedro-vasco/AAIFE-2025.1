import argparse
from leitura.leitor_historico import carregar_historico
from processamento.agrupador import analisar_categorias, identificar_bolha_e_dominantes # Importe a nova função
from processamento.gerador_sugestoes import gerar_sugestoes_diversificadas
from exportacao.exportador_json import exportar_sugestoes_json


def main():
    parser = argparse.ArgumentParser(description="Recomendador de vídeos diversificados no YouTube")
    parser.add_argument("--input", required=True, help="Caminho para o arquivo JSON do histórico")
    parser.add_argument("--output", required=True, help="Caminho para o arquivo JSON de saída")
    parser.add_argument("--base", default="data/base_simulada.json", help="Base simulada de vídeos (opcional)")
    parser.add_argument("--threshold_individual", type=float, default=0.6,
                        help="Threshold de dominância para categoria individual (RF03).")
    parser.add_argument("--threshold_soma_top_n", type=float, default=0.8,
                        help="Threshold para soma das proporções das N categorias mais dominantes.")
    parser.add_argument("--n_top_categorias", type=int, default=3,
                        help="Número de categorias mais dominantes a considerar para o threshold_soma_top_n.")
    parser.add_argument("--limite", type=int, default=10, help="Número máximo de sugestões.")

    args = parser.parse_args()

    print("[INFO] Carregando histórico do usuário...")
    historico = carregar_historico(args.input)

    print(f"[INFO] Analisando {len(historico)} vídeos assistidos para identificar bolhas...")
    # Chame a função analisar_categorias com os novos parâmetros
    agrupamento, dominantes, bolha_identificada = analisar_categorias(
        historico,
        threshold_categoria_individual=args.threshold_individual,
        threshold_soma_categorias_top_n=args.threshold_soma_top_n,
        n_top_categorias=args.n_top_categorias
    )

    print(f"[INFO] Categorias dominantes (critério individual): {dominantes}")
    if bolha_identificada:
        print("[ALERTA] Uma bolha social/algorítmica foi identificada com base no seu consumo de conteúdo. ")
    else:
        print("[INFO] Nenhuma bolha social/algorítmica significativa identificada neste histórico. ")

    print("[INFO] Carregando base simulada para sugestões...")
    base_simulada = carregar_historico(args.base)

    print("[INFO] Gerando sugestões diversificadas para 'estourar a bolha' (se houver)... ")
    sugestoes = gerar_sugestoes_diversificadas(historico, dominantes, base_simulada, limite=args.limite)

    print(f"[INFO] Exportando {len(sugestoes)} sugestões para JSON...")
    exportar_sugestoes_json(sugestoes, args.output)

    print("[OK] Processo concluído com sucesso!")


if __name__ == "__main__":
    main()