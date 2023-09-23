!pip -q install langchain openai
import os
#replace "YOUR_OPENAI_API_KEY" with your own api key from OPENAI
os.environ["OPENAI_API_KEY"] = "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"
!pip show langchain
import pandas as pd
from google.colab import files

# Upload holding.csv and trades.csv files
uploaded = files.upload()
# Load CSV data into a Pandas DataFrame
df1 = pd.read_csv('holdings.csv')
df2 = pd.read_csv('trades.csv')
# Now, you can work with df1 and df2 in your analysis and training
# For example, you can print the first few rows of each dataframe
print("DataFrame 1:")
print(df1.head())
print("DataFrame 2:")
print(df2.head())
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
#Create a variable and set the OPENAI temperature to '0' for accurate response
llm = OpenAI(temperature=0)
#creating a list called agents = [] to store 'n' number of files
agents = [
      create_csv_agent(OpenAI(temperature=0), 'holdings.csv', verbose=True),
         create_csv_agent(OpenAI(temperature=0), 'trades.csv', verbose=True)
          ]

agents

agents[0].agent.llm_chain.prompt.template
agents[1].agent.llm_chain.prompt.template
#enter your query related to the csv file provided above
user_input = input("Enter question: ")

response_from_agent0 = agents[0].run(user_input)
response_from_agent1 = agents[1].run(user_input)
# Check if the user's question is found in both agents
if response_from_agent0 and response_from_agent1:
# If the question is found in both agents, combine the responses
    combined_response = f"From holdings.csv: {response_from_agent0}\nFrom trades.csv: {response_from_agent1}"
    print("The answer is found in both the csv files!")
    print(combined_response)
elif response_from_agent0:
# If the question is found only in the first agent, print its response
    print("Response from holdings.csv:")
    print(response_from_agent0)
elif response_from_agent1:
# If the question is found only in the second agent, print its response
    print("Response from trades.csv:")
    print(response_from_agent1)
else:
# If the question is not found in either agent
    print("Sorry, information not found.")
