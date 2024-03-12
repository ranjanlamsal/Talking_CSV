#csvreader.py

from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI
import os


def prompt_response(user_prompt, file):
    """
    Prompts a response based on the user's input and the data in the CSV file.

    Parameters:
        user_prompt (str): The user's input to generate a response.
        file (str): The path to the CSV file containing data.

    Returns:
        str: The generated response based on the user's input and data from the CSV file.
        
    """
    agent = create_csv_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        file,
        verbose=False,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    response = agent.invoke(user_prompt)
    print(response['output'])
    return response['output']
