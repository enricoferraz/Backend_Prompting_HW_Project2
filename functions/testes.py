import requests

#create a session to allow JS execution
session = requests.Session()

# Define the headers to avoid being blocked
headers = {
    "User-Agent": "Chrome/133.0.6943.127",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html"
}

slugs = ["littlejohn-v-state-7","beattie-v-beattie", "travelers-indem-co-v-lake", "tilden-v-state", "in-re-lee-342013"]

for slug in slugs:
    url_case_text = f'https://casetext.com/api/search-api/doc/{slug}/html'
    response = session.get(url_case_text, headers=headers)
    print(url_case_text)

    print(response.cookies, response.status_code)
    break

