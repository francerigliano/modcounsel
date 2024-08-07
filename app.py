import pandas as pd
from flask import Flask, request, render_template
from pandasai import Agent
import os

# Configuration of PANDAS API KEY
os.environ["PANDASAI_API_KEY"] = "$2a$10$e68cf6iSorLhkvXjRF3Fu.97WcqplKAoZcIziy8CCHAuea7Tn0w2y"

# Read Excel file
df = pd.read_excel('Movie Data.xlsx')

# Start PandasAI Agent
agent = Agent(df)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        # Use agent to search for result
        result = agent.chat(query)
        
        # Convert the result to a list of titles if its a DataFrame
        if isinstance(result, pd.DataFrame):
            results = result['Movie Title'].tolist()
        else:
            results = [result]  # For results that are not DataFrame
        
        return render_template('index.html', query=query, results=results)
    return render_template('index.html', query='', results=[])

if __name__ == '__main__':
    app.run(debug=True)
