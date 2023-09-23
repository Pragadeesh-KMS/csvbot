
# README for CSV Query Tool

This Python script is a CSV query tool that allows you to search for information in two CSV files using the OpenAI GPT-3 language model. It provides responses based on user queries related to the content of these CSV files.

**Incase you are using Google colab for testing:**
- [![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16tCivijJ2n6xqwuyYnv3_lIeybGJeCTX?usp=sharing)
- [COLAB_README.md](https://github.com/Pragadeesh-KMS/csvbot/blob/main/COLAB_README.md)



## Usage

1. **Clone the Repository**

   To get started, you'll need to clone or download this repository to your local machine. Follow these steps:

   - Open a terminal/command prompt.
   - Navigate to the directory where you want to store the repository.
   - Use the following command to clone the repository:

     ```shell
     git clone https://github.com/Pragadeesh-KMS/csvbot.git
     ```
2. **Change directory**
   ```bash
   cd csvbot
   ```

4. **Install Dependencies**

   Before running the script, ensure you have Python and the required libraries installed. You can install the necessary libraries using `pip`:

   ```shell
   pip install pandas langchain openai
   ```
5. **Open python file**
   ```bash
   python bot.py
   ```

This Python script is a CSV query tool that allows you to search for information in two CSV files using the OpenAI GPT-3 language model. It provides responses based on user queries related to the content of these CSV files.

## Code Explanation

### Importing Libraries

```python
import os
import pandas as pd
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
```

- `os` is imported to handle environment variables.
- `pandas` is imported for working with CSV data.
- `create_csv_agent` and `OpenAI` are imported from external modules for creating agents and using the OpenAI GPT-3 language model.

### Getting OpenAI API Key

```python
openai_api_key = input("Enter your OpenAI API key: ")
os.environ["OPENAI_API_KEY"] = openai_api_key
```

- The script prompts the user to enter their OpenAI API key and sets it as an environment variable.

### Getting Paths to CSV Files

```python
holdings_csv_path = input("Enter the path to your csv file: ")
trades_csv_path = input("Enter the path to your csv file: ")
```

- Users are prompted to enter the file paths for two CSV files: `holdings.csv` and `trades.csv`.

### Loading CSV Data

```python
df1 = pd.read_csv(holdings_csv_path)
df2 = pd.read_csv(trades_csv_path)
```

- The script uses `pandas` to read the CSV data from the specified file paths and stores them in DataFrames (`df1` and `df2`).

### Creating Agents

```python
agent1 = create_csv_agent(OpenAI(temperature=0), holdings_csv_path, verbose=True)
agent2 = create_csv_agent(OpenAI(temperature=0), trades_csv_path, verbose=True)
```

- Agents are created using the OpenAI GPT-3 model with a temperature setting of 0 for both CSV files. These agents are designed to respond to queries related to the CSV content.

### User Input and Querying

```python
user_input = input("Enter question: ")
```

- Users can input their query related to the CSV files.

### Running Queries on Agents

```python
response_from_agent1 = agent1.run(user_input)
response_from_agent2 = agent2.run(user_input)
```

- The user's query is executed on both agents, resulting in responses.

### Displaying Responses

```python
if response_from_agent1 and response_from_agent2:
    combined_response = f"From holdings.csv: {response_from_agent1}\nFrom trades.csv: {response_from_agent2}"
    print("The answer is found in both the CSV files!")
    print(combined_response)
elif response_from_agent1:
    print("Response from holdings.csv:")
    print(response_from_agent1)
elif response_from_agent2:
    print("Response from trades.csv:")
    print(response_from_agent2)
else:
    print("Sorry, information not found.")
```

- The script checks if there are responses from both agents and displays a combined response if available.
- If there's a response from only one agent, it displays that response.
- If no responses are found, it informs the user that the information was not found in either CSV file.

## Remember

1. Make sure you have Python and the required libraries installed.
2. Obtain an OpenAI API key and enter it when prompted.
3. Provide the paths to your `holdings.csv` and `trades.csv` files.
4. Enter your query, and the script will provide responses based on the CSV data.

Note: Ensure that you have the necessary dependencies and permissions to use the OpenAI GPT-3 API and access the CSV files.
