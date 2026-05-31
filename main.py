from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
#from pprint import pprint

load_dotenv()

@tool
def calculate_age(year:int)->str:
    """Calcula edad basada en el año de nacimiento."""

    return f"Edad aproximada: {2026-year}"

llm = ChatOpenAI(
    model="gpt-4.1-mini"
)

agent = create_agent(
    model = llm,
    tools=[calculate_age],
    debug=True
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Nací en Marzo de 1991. ¿Qué edad tengo?"
            }
        ]
    }
)

print(response)
#pprint(response)