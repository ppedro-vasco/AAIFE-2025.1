// src/components/FileUpload.jsx
import { useState } from 'react';
import axios from 'axios';

function FileUpload({ onUploadComplete, onAnalysisStart, isLoading }) {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        // Pega o primeiro arquivo selecionado
        if (event.target.files && event.target.files[0]) {
            setSelectedFile(event.target.files[0]);
        }
    };

    const handleUpload = async () => {
        if (!selectedFile) return;

        onAnalysisStart(); // Avisa o componente pai que a análise começou

        const formData = new FormData();
        formData.append('history_file', selectedFile);

        try {
            const response = await axios.post('http://localhost:5000/api/analyze', formData);
            onUploadComplete(response.data);
        } catch (error) {
            console.error("Erro ao fazer upload:", error);
            onUploadComplete(null);
            alert('Ocorreu um erro ao analisar o arquivo.');
        }
    };

    return (
        <div className="bg-metal p-6 rounded-lg space-y-4">
            {/* Botão para abrir o seletor de arquivos */}
            <label htmlFor="file-upload" className="w-full text-center font-orbitron text-lg text-glow-green uppercase py-3 rounded-md btn-metal cursor-pointer block">
                {/* Texto dinâmico: mostra o nome do arquivo ou o texto padrão */}
                {selectedFile ? `ARQUIVO: ${selectedFile.name}` : '[ CARREGAR HISTÓRICO ]'}
            </label>
            <input id="file-upload" type="file" onChange={handleFileChange} accept=".json" className="hidden" />

            {/* Botão de Análise, desabilitado se não houver arquivo */}
            <button onClick={handleUpload} disabled={!selectedFile || isLoading} className="w-full font-orbitron text-lg text-glow-orange uppercase py-3 rounded-md btn-metal disabled:opacity-50 disabled:cursor-not-allowed">
                {isLoading ? '[ ANALISANDO... ]' : '[ INICIAR ANÁLISE ]'}
            </button>
        </div>
    );
}

export default FileUpload;