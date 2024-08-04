import requests
from bs4 import BeautifulSoup
import pyttsx3

urls = {
    'technology': 'https://indianexpress.com/section/technology/gadgets/',
    'sports': 'https://indianexpress.com/section/sports/',
    'education': 'https://indianexpress.com/section/education/',
    'business': 'https://indianexpress.com/section/business/',
    'political': 'https://indianexpress.com/section/political-pulse/',
    'entertainment': 'https://indianexpress.com/section/entertainment/'
}

def fetch(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', class_='nation')
    headings = div.find_all('h2', class_='title')
    data = []
    for heading in headings:
        link_tag = heading.find('a')
        text = link_tag.get_text().strip()
        link = link_tag['href']
        data.append((text, link))
    return data

def news(headings):
    engine = pyttsx3.init()
    for heading, link in headings:
        print(heading)
        engine.say(heading)
        engine.runAndWait()
        print(f"Link: {link}")
        print()

def main():
    choice = input("Enter a topic (technology, sports, education, business, political, entertainment) or any key: ").strip().lower()
    if choice in urls:
        headings = fetch(urls[choice])
        news(headings)
    else:
        all_news = []
        for url in urls.values():
            all_news.extend(fetch(url))
        news(all_news)

if __name__ == "__main__":
    main()
