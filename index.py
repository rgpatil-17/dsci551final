"""The interface file
"""

import gradio as gr

from app.functions.query_handler import execute_query
from app.functions.data_modifier import modify_data as md
from app.functions.schema_explorer import explore_schema as es

# Functions
def ask_question(query: str):
    """This function is responsible in executing the read-only queries

    Parameters
    ----------
    query : str
        query from the user

    Returns
    -------
    str
        response from llm
    """
    try:
        result = execute_query(natural_language_query=query)
        return f"Answer to your question: {result}"
    except Exception as e:
        print(e)
        return "Unfortunately, the provided schema doesn't contain information about this criteria."

def modify_data(data: str):
    """This function is responsible in executing the write-only queries

    Parameters
    ----------
    data : str
        data from the user

    Returns
    -------
    str
        response from llm
    """
    try:
        response = md(natural_language_command=data)
        return f"Data modification request: {response}"
    except Exception as e:
        print(e)
        return "Unfortunately, the provided schema doesn't contain information about this criteria."

def explore_schema(query: str):
    """This function is responsible in exploring schema and database

    Parameters
    ----------
    query : str
        query from the user

    Returns
    -------
    str
        response from llm
    """
    try:
        result = es(user_question=query)
        return f"Answer to your question: {result}"
    except Exception as e:
        print(e)
        return "Unfortunately, the provided schema doesn't contain information about this criteria."

# Create Gradio Interface
def create_ui():
    """The function is responsible in preparing the interface for the user
    """
    with gr.Blocks() as demo:
        # Title for the page
        gr.Markdown("## NBA Natural Language SQL Bot")

        # Ask a question section
        gr.Markdown("### Ask a question")
        query_input = gr.Textbox(label="Ask a question")
        query_button = gr.Button("Submit")
        query_output = gr.Textbox(label="Answer", interactive=False)

        # Modify data section
        gr.Markdown("### Modify Data")
        modify_input = gr.Textbox(label="Modify Data")
        modify_button = gr.Button("Submit")
        modify_output = gr.Textbox(label="Modification Response", interactive=False)

        # Explore Schema/Database section
        gr.Markdown("### Explore Schema/Database")
        explore_input = gr.Textbox(label="Explore Schema/Database")
        explore_button = gr.Button("Submit")
        explore_output = gr.Textbox(label="Response", interactive=False)

        # Bind functions to buttons
        query_button.click(ask_question, inputs=query_input, outputs=query_output)
        modify_button.click(modify_data, inputs=modify_input, outputs=modify_output)
        explore_button.click(explore_schema, inputs=explore_input, outputs=explore_output)

    demo.launch()

# Run the UI
create_ui()
