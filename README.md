This is a Master File for ModCounsel technical challenge. In this challenge, a search bar was designed and built using a large language model with the PandasAI library (https://docs.pandas-ai.com/intro). This library allows for quick and efficient prototyping using the provided Excel file. It is a generative AI model that understands and interprets natural language queries and translates them into Python code and SQL queries. It then uses the code to interact with the data and return the results to the user. The same Excel file is previously processed with the following Python code in a Jupyter Notebook.

import pandas as pd

def clean_data(df):
	for column in df.columns:
		if df[column].dtype == 'object':
		df[column] = df[column].str.replace(',', '')
		df['Release Year'] = pd.to_numeric(df['Release Year'], 				errors='coerce')
		df['Budget (millions $)'] = pd.to_numeric(df['Budget (millions 		$)'], errors='coerce')
		df['Rotten Tomatoes Score'] = pd.to_numeric(df['Rotten Tomatoes 		Score'], errors='coerce')
		df.dropna(inplace=True)
	return df

df_cleaned = clean_data(df)
print(df_cleaned)

cleaned_file_path = 'Movie Data.xlsx'
df_cleaned.to_excel(cleaned_file_path, index=False, engine='openpyxl')


It is noteworthy that this library has a limit of 100 requests per query per month per account, but for the purposes of this challenge, it was considered sufficient.

Explain what you could have done better next time?

Next time, a Large Language Model (LLM) with the Langchain framework and the OpenAI API could be used. In this challenge, all free tools were used.

What part of the application was the hardest to build?

The hardest part of the application was finding a natural language processing method that could be applied quickly and effectively. Various possible queries were tried, and the results were verified with the same open Excel file.

What part of the application was the easiest to build?

Programming the HTML file that serves as the front-end of the website to be designed was not particularly difficult. It should be noted that a quick design was sought without considering its aesthetics.

What took the most time to complete?

Most of the time was spent thinking about which backend solution to apply. Various NLP and LLM tools, such as the use of Transformers, were experimented with.

What would you change about your application if you had more time?

Consider how to use an LLM model more efficiently.
