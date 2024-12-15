import requests
import validators
from bs4 import BeautifulSoup

def extract_html(url):
    if validators.url(url):
        try:
            res = requests.get(url)
            if res.status_code != 200:
                return "Sorry! The link cannot be accessed."
            else:
                return res.text
        except requests.exceptions.RequestException:
            return "There was an error while attempting to make a request."
    else:
        return "Invalid URL"

def extract_text(url):
    if validators.url(url):
        try:
            res = requests.get(url)
            if res.status_code != 200:
                return "Sorry! The link cannot be accessed."
            else:
                soup = BeautifulSoup(res.text, "lxml")
                formatted_text = format_content(soup)
                return formatted_text
        except requests.exceptions.RequestException:
            return "There was an error while attempting to make a request."
    else:
        return "Invalid URL"

def extract_headings(url):
    if validators.url(url):
        try:
            res = requests.get(url)
            if res.status_code != 200:
                return "Sorry! The link cannot be accessed."
            else:
                soup = BeautifulSoup(res.text, "lxml")
                headings = ''
                for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                    headings += tag.get_text(separator="\n") + '\n'
                return headings.strip()
        except requests.exceptions.RequestException:
            return "There was an error while attempting to make a request."
    else:
        return "Invalid URL"

def extract_links(url):
    if validators.url(url):
        try:
            res = requests.get(url)
            if res.status_code != 200:
                return "Sorry! The link cannot be accessed."
            else:
                soup = BeautifulSoup(res.text, "lxml")
                links = ''
                for tag in soup.find_all('a', href=True):
                    link = tag.get('href')
                    if link:
                        links += f"{tag.get_text()} - {link}\n"
                return links.strip()
        except requests.exceptions.RequestException:
            return "There was an error while attempting to make a request."
    else:
        return "Invalid URL"

def extract_by_tag(url, tag_name):
    if validators.url(url):
        try:
            res = requests.get(url)
            if res.status_code != 200:
                return "Sorry! The link cannot be accessed."
            else:
                soup = BeautifulSoup(res.text, "lxml")
                elements = soup.find_all(tag_name)
                extracted_text = ''
                for element in elements:
                    extracted_text += element.get_text() + '\n'
                return extracted_text
        except requests.exceptions.RequestException:
            return "There was an error while attempting to make a request."
    else:
        return "Invalid URL"

def format_content(soup):
    formatted_text = ""

    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        formatted_text += f"{heading.get_text()}\n"

    for p in soup.find_all('p'):
        formatted_text += f"{p.get_text()}\n"

    for list_tag in soup.find_all(['ul', 'ol']):
        formatted_text += "\n"
        for li in list_tag.find_all('li'):
            formatted_text += f" - {li.get_text()}\n"

    formatted_text += "\nLinks:\n"
    for link in soup.find_all('a', href=True):
        link_text = link.get_text(strip=True)
        link_url = link.get('href')
        if link_text and link_url.startswith('http'):
            formatted_text += f"{link_text} - {link_url}\n"

    return formatted_text.strip()
