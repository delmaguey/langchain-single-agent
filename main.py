from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from src.tools.age_tool import calculate_age
#from pprint import pprint


load_dotenv()

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