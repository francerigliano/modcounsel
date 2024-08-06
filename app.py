import pandas as pd
from flask import Flask, request, render_template
from pandasai import Agent
import os

# Configurar la clave API de PandasAI
os.environ["PANDASAI_API_KEY"] = "$2a$10$e68cf6iSorLhkvXjRF3Fu.97WcqplKAoZcIziy8CCHAuea7Tn0w2y"

# Leer el archivo Excel
df = pd.read_excel('Movie Data.xlsx')

# Inicializar el agente de PandasAI
agent = Agent(df)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        # Usar el agente de PandasAI para buscar
        result = agent.chat(query)
        return render_template('index.html', query=query, results=result)
    return render_template('index.html', query='', results='')

if __name__ == '__main__':
    app.run(debug=True)
