import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content": """
            Classifique o produto abaixo em uma das categorias: Higiene Pessoal, Moda ou Casa. De uma descrição da categoria.
            """
        },
        {
            "role" : "user",
            "content": """
            Escova de dentes de bambu
            """
        }
    ],
    model="gpt-4",
    temperature=0,
    max_tokens=200,
    n = 3
)
for contador in range(0,3):
    print(resposta.choices[contador].message.content)