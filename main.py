from functions.chatgpt_api import get_response_from_gpt
from functions.get_html_from_slug import get_text_from_decisions

slugs = ["littlejohn-v-state-7","beattie-v-beattie", "travelers-indem-co-v-lake", "tilden-v-state", "in-re-lee-342013"]


def extract_negative_treatments(slug: str) -> str | dict:
    #Get decision text from html
    decision = get_text_from_decisions(slug)
    #Return gpt's response
    return get_response_from_gpt(decision)


for slug in slugs:
    treatments = extract_negative_treatments(slug=slug)
    print(slug +"\n" , treatments)
    





