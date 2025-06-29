// src/components/MainPanel.jsx
import { useState } from 'react';
import FileUpload from './FileUpload.jsx';
import ResultsDisplay from './ResultsDisplay.jsx';

function MainPanel() {
    const [analysisResult, setAnalysisResult] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleAnalysisComplete = (resultData) => {
        setAnalysisResult(resultData);
        setIsLoading(false); // Para o loading quando o resultado chega
    };

    const handleAnalysisStart = () => {
        setIsLoading(true);
        setAnalysisResult(null); // Limpa resultados antigos
    }

    return (
        <div className="flex flex-col gap-8">
            {/* Se não houver resultado, mostra o upload. Se houver, mostra os resultados */}
            {!analysisResult ? (
                <FileUpload
                    onUploadComplete={handleAnalysisComplete}
                    onAnalysisStart={handleAnalysisStart}
                    isLoading={isLoading}
                />
            ) : (
                <ResultsDisplay result={analysisResult} />
            )}
        </div>
    );
}

export default MainPanel;