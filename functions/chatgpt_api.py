from openai import OpenAI
from entities.prompts import prompt_1, prompt_2
from entities import NegativeTreatment
from dotenv import load_dotenv
import os
import json

load_dotenv('.env')

client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))

def get_response_from_gpt(decision: str) -> str | dict:
    #Using 4o-mini as its cheaper and better than 3.5-turbo
    #Also accepts strutured outputs
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {
                "role": "system", 
                "content": prompt_2
            },
            {
                "role": "user", 
                "content": decision
            }
        ],
        response_format=NegativeTreatment
    )

    return json.dumps(json.loads(response.choices[0].message.content), indent=2)