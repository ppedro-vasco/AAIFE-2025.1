// src/components/ResultsDisplay.jsx
import React from 'react';
import SuggestionCard from './SuggestionCard.jsx';

function ResultsDisplay({ result }) {
    // Se ainda não houver resultado, não exibe nada.
    if (!result) {
        return null;
    }

    const { analysis, suggestions } = result;

    // Mapeia a severidade para a cor do brilho do texto
    const severityGlowClass = {
        'Alta': 'text-glow-orange',
        'Média': 'text-yellow-400', // Usando uma cor padrão do tailwind para média
        'Baixa': 'text-glow-green',
    }[analysis.severity] || 'text-white';


    return (
        <div className="space-y-8">
            {/* Painel de Análise, estilizado como o Alerta */}
            <div className="border-2 border-dashed border-orange-500/50 p-6 rounded-md text-center">
                <p className={`font-orbitron font-bold text-xl uppercase ${severityGlowClass}`}>
                    !! ALERTA: CÂMARA DE ECO DETECTADA !!
                </p>
                <p className="text-md text-gray-400 mt-2">
                    Nível de Severidade: <span className="font-bold">{analysis.severity}</span> | Entropia: {analysis.entropy}
                </p>
            </div>

            {/* Seção de Sugestões */}
            <div>
                <h2 className="font-orbitron text-2xl font-bold text-white mb-4 text-center">SUGESTÕES DE CONTEÚDO:</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {suggestions.map((suggestion) => (
                        <SuggestionCard key={suggestion.video_id} suggestion={suggestion} />
                    ))}
                </div>
            </div>
        </div>
    );
}

export default ResultsDisplay;