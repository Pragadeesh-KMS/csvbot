import os
import pandas as pd
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Get paths to CSV files from user input
holdings_csv_path = input("Enter the path to holdings.csv: ")
trades_csv_path = input("Enter the path to trades.csv: ")

# Load CSV data into Pandas DataFrames
df1 = pd.read_csv(holdings_csv_path)
df2 = pd.read_csv(trades_csv_path)

# Create agents for CSV files
agent1 = create_csv_agent(OpenAI(temperature=0), holdings_csv_path, verbose=True)
agent2 = create_csv_agent(OpenAI(temperature=0), trades_csv_path, verbose=True)

# Enter your query related to the CSV files
user_input = input("Enter question: ")

# Run the query on both agents
response_from_agent1 = agent1.run(user_input)
response_from_agent2 = agent2.run(user_input)

# Check if the user's question is found in both agents
if response_from_agent1 and response_from_agent2:
    # If the question is found in both agents, combine the responses
    combined_response = f"From holdings.csv: {response_from_agent1}\nFrom trades.csv: {response_from_agent2}"
    print("The answer is found in both the CSV files!")
    print(combined_response)
elif response_from_agent1:
    # If the question is found only in the first agent, print its response
    print("Response from holdings.csv:")
    print(response_from_agent1)
elif response_from_agent2:
    # If the question is found only in the second agent, print its response
    print("Response from trades.csv:")
    print(response_from_agent2)
else:
    # If the question is not found in either agent
    print("Sorry, information not found.")
