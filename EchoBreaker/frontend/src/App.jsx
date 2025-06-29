// src/App.jsx
import Header from './components/Header.jsx';
import MainPanel from './components/MainPanel.jsx';

function App() {
  return (
    // O container principal
    <div className="max-w-5xl mx-auto border-2 border-t-4 border-lime-400/50 rounded-lg overflow-hidden bg-black/30 backdrop-blur-sm text-gray-300">
      <Header />

      {/* O main agora é uma única coluna, o MainPanel ocupará todo o espaço */}
      <main className="p-6 sm:p-8">
        <MainPanel />
      </main>
    </div>
  );
}

export default App;