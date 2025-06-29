// src/components/SuggestionCard.jsx
import React from 'react';

function SuggestionCard({ suggestion }) {
    const videoUrl = `https://www.youtube.com/watch?v=${suggestion.video_id}`;

    return (
        // 1. Adicionamos a classe 'group' para o hover funcionar no 'div' filho.
        // 2. Adicionamos as classes de transição e hover para o efeito de elevação.
        <div className="relative group bg-black/50 border-2 border-lime-400/50 rounded-lg p-4 shadow-lg shadow-lime-400/10 flex flex-col justify-between h-full transition-transform duration-200 ease-in-out hover:-translate-y-1">

            {/* 3. Adicionamos 'group-hover' para intensificar o brilho e a transição para suavidade. */}
            <div className="absolute -inset-0.5 bg-lime-400 rounded-lg blur opacity-20 group-hover:opacity-60 group-hover:blur-md transition duration-200 ease-in-out"></div>

            {/* O conteúdo do card precisa continuar relativo para ficar por cima do brilho */}
            <div className="relative">
                <h4 className="font-orbitron font-bold text-lg text-lime-300 mb-2">
                    <a href={videoUrl} target="_blank" rel="noopener noreferrer" className="hover:underline">
                        {suggestion.title}
                    </a>
                </h4>
                <p className="font-exo text-sm text-gray-400">Canal: {suggestion.channel}</p>
                <p className="font-exo text-sm text-gray-400">Categoria: {suggestion.category}</p>
                <div className="mt-3 border-t border-gray-700 pt-3">
                    <p className="font-exo text-xs text-gray-200 italic">
                        {suggestion.justification}
                    </p>
                </div>
            </div>
        </div>
    );
}

export default SuggestionCard;