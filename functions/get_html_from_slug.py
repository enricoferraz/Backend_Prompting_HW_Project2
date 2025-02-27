import requests
from bs4 import BeautifulSoup


#create a session to allow JS execution
session = requests.Session()

# Define the headers to avoid being blocked
headers = {
    "User-Agent": "Chrome/133.0.6943.127"
}

def get_full_text(full_text: BeautifulSoup) -> str:
    #List to save the decision's chunks
    decision_chunks = []

    decision_sections = full_text.find_all("section", class_="decision opinion")
    # Extract and return decision's full text in str
    for section in decision_sections:
        text = section.get_text(separator="\n", strip=True)
        decision_chunks.append(f"{text}\n")
    return "\n".join(decision_chunks)


def get_text_from_decisions(slug: str) -> str:
    # Try to get data from the slug url
    url_case_text = f'https://casetext.com/api/search-api/doc/{slug}/html'
    response = session.get(url=url_case_text, headers=headers)

    #If authorized
    if response.status_code == 200 and response.text != "":
        # Extract the text from html
        full_text = BeautifulSoup(response.text, 'html.parser')

        return get_full_text(full_text)
    
    #If forbidden, get from slugs directory
    if response.status_code == 403:
        #Read from slug file
        with open(f'slugs//{slug}.htm', 'r') as file:
            full_text = BeautifulSoup(file, 'html.parser')
              
        return get_full_text(full_text)

    
        
