import requests
from bs4 import BeautifulSoup

def get_program_links(url, BASE_URL):
    links = []
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the funding program divs
        program_divs = soup.find_all('div', class_='card card--horizontal card--fundingprogram')
        
        for div in program_divs:
            link = div.find('a', title='Öffnet die Einzelsicht')
            if link:
                href = link.get('href')
                full_link = BASE_URL + href
                links.append(full_link)
        
        # Find the "weiter" link
        next_link = soup.find('a', class_='forward button', title='SucheSeite')
        if next_link:
            url = BASE_URL + next_link.get('href')
        else:
            url = None
    
    return links


def extract_program_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    program_details = {}

    name_tag = soup.find('h1', class_='title')
    program_details["name"] = name_tag.get_text(strip=True) if name_tag else "No Name Found"

    tab_names = [tab_h2.get_text().lower().strip() for tab_h2 in soup.find_all("h2", class_="horizontal--tab-opener")]

    articles = soup.find_all("article", class_="content--tab-text")
    for i in range(len(articles)):
        tab_content = []
        for child in articles[i].descendants:
            if child.name in ['p', 'h3']:
                tab_content.append(child.get_text(strip=True))
        program_details[tab_names[i]] = "\n".join(tab_content)

    return program_details