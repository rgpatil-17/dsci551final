# Natural Language SQL Bot for NBA


## Introduction
This project enables users to interact with a MySQL database using natural language. Users can create, read, update, and delete data by simply typing commands in plain English. The system translates these commands into SQL queries and executes them securely against the database.

## Features
- Understands natural language input
- Connects to a MySQL database
- Supports CRUD operations (Create, Read, Update, Delete)
- Built with Python
- Easily extensible for new data sources or models


## Tech Stack
- Language: Python
- Database: MySQL
- UI: Gradio
- Environment: Virtualenv or venv
- LLM: llama3.2 from ollama

## Setup Instructions
- To get started you need a Python interpreter with Python 3.10 or above and the correct packages installed. 

- The recommended way to go about this is to use a [virtualenv](https://virtualenv.pypa.io/en/latest/) virtual environment. For this to work, you will first need
a working [Python 3.10](https://www.python.org/downloads/) installation on your system.

- To setup the project please follow the following steps :

### 1. Clone the Repository
`git clone https://github.com/rgpatil-17/dsci551final.git`

### 2. Create and Activate Virtual Environment
`python -m venv venv`
`source venv/bin/activate  # On Windows: venv\Scripts\activate`

NOTE: Use `python3.10` instead of `python` if you need a virtual environment with python3.10.

### 3. Install Dependencies
`pip install -r requirements.txt`

- To add packages, you simply use `pip3 install <PACKAGE_NAME>` to add them to your environment.
NOTE: Always perform `pip freeze > requirements.txt` right after adding or removing any packages in order to keep it clean and up to date.

### 4. Configure Environment Variables
Create a .env file and set the following variables:
`DB_NAME="NBA_DB"`
`DB_USER="root"`
`DB_PASSWORD=""`
`DB_HOST="127.0.0.1:3306"`

### 5. Setup Ollama in your local system
A. Install Ollama
For MacOS: 
- `brew install ollama`

For Ubuntu/Linux: 
- `curl -fsSL https://ollama.com/install.sh | sh`

For Windows: 
- Go to `https://ollama.com/download/windows` and click on `Download For Windows`
- Run the installer.
- After installation, open Command Prompt or PowerShell.

B. Verify Installation
`ollama --version`

You should see the version printed, e.g., ollama version 0.1.34.

C. Start the Ollama Service
Just run `ollama run llama3.2`

This will:
- Download the model the first time (~4–8 GB depending on quantization)
- Start the model and run it interactively

You can stop it with Ctrl+C.
If you just want to pull the model for now then run `ollama pull llama3.2`

D. Tips
- List installed models: `ollama list`
- Remove a model : `ollama rm llama3.2`
- Optional: Run Ollama in the background: `ollama serve`


### 6. Run the Application
`python index.py`

This will start the service (CLI or web-based depending on your implementation). You will a message : `Running on local URL:  http://127.0.0.1:7860`. 
Copy the url and paste on the browser and it will let you enter natural language commands.

## Example Usage
- Input: “Show me all teams with their ids and cities”

- SQL Generated: SELECT team_id, city, team_name FROM teams; 

- Output: 
team_id,team_name,city
200,"Atlanta Hawks",Atlanta
201,"Boston Celtics",Boston
202,"Brooklyn Nets",Brooklyn
203,"Charlotte Hornets",Charlotte
204,"Chicago Bulls",Chicago
205,"Cleveland Cavaliers",Cleveland



## Project Structure
project
|

|__ app

|

|_________|___ functions

|_______|_________|___ data_modifier.py     # Modify Data

|_______|_________|___ query_modifier.py    # Read Data

|_______|_________|___ schema_explorer.py   # Explore Schema

|_________|___ config.py                     # Configurations File

|_________|___ llm.py                        # Connection to llm

|__ index.py                      # Main entry point

|__ .gitignore                    # GitIgnore 

|__ README.md                     # You're reading this

|__ .env.development              # environment variables

|__ requirements.txt              # includes Python dependencies



## Contributing
- Feel free to fork this repo, open issues, or submit pull requests.
