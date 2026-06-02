from langchain.tools import tool

@tool
def calculate_age(year:int)->str:
    """Calcula edad basada en el año de nacimiento."""

    return f"Edad aproximada: {2026-year}"