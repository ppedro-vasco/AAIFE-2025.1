// src/components/Header.jsx
import React from 'react';

function Header() {
    return (
        <header className="p-6 sm:p-8 border-b-2 border-lime-400/50">
            {/* Container Flex para alinhar título e logo */}
            <div className="flex items-center justify-center gap-4 sm:gap-6">
                <h1 className="font-orbitron text-4xl sm:text-5xl font-black uppercase tracking-widest text-glow-green">
                    ECHO<span className="text-glow-orange">BREAKER</span>
                </h1>
                {/* Logo SVG com tamanho ajustado */}
                <div className="relative w-12 h-12 sm:w-16 sm:h-16">
                    <svg className="absolute inset-0" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M98 50C98 76.51 76.51 98 50 98S2 76.51 2 50 23.49 2 50 2" stroke="#00ff9d" strokeWidth="4" strokeLinecap="round" />
                        <path d="M60 20L85 5" stroke="#ff4d00" strokeWidth="5" strokeLinecap="round" />
                        <path d="M75 35L95 25" stroke="#ff4d00" strokeWidth="5" strokeLinecap="round" />
                    </svg>
                </div>
            </div>
            {/* Subtítulo com mais espaçamento e cor chamativa */}
            <p className="font-exo mt-4 text-lg text-lime-400 uppercase tracking-wider text-center">
                Desafie a Realidade. Quebre o Sistema.
            </p>
        </header>
    );
}

export default Header;