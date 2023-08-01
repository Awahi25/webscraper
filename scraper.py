import requests
from bs4 import BeautifulSoup
from business import Business

def scrape_website(url):
    # Send a request to the website
    r = requests.get(url)

    # Parse the website using Beautiful Soup
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find business information on the webpage. Replace 'tag' and 'class' with the correct tag and class for the specific website
    business_elements = soup.find_all('tag', class_='class')

    businesses = []
    for element in business_elements:
        name = element.find('tag', class_='class').text.strip()
        address = element.find('tag', class_='class').text.strip()
        phone_number = element.find('tag', class_='class').text.strip()
        email = element.find('tag', class_='class').text.strip()
        website = element.find('tag', class_='class').text.strip()

        businesses.append(Business(name, address, phone_number, email, website))

    return businesses
