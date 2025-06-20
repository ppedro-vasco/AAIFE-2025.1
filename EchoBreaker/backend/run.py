from src import app

if __name__ == '__main__':
    # Inicia o servidor Flask.
    # host = '0.0.0.0' permite que o servidor seja acessível na sua rede local.
    # port = 5000 é a porta padrão do Flask.
    app.run(host='0.0.0.0', port=5000)