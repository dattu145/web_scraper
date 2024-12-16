# Web Scraper

A simple web scraper built using Flask that allows users to extract data from websites.

## Features
- Easy to set up and use.
- Built with Flask for a lightweight web server.
- Flexible scraping logic to suit various needs.

### Libraries Required :

##### 1. requests

Purpose: Simplifies making HTTP requests (GET, POST, PUT, DELETE, etc.).
Use Cases: Fetching data from APIs, scraping basic web content.

##### 2. validators

Purpose: Validates data such as URLs, email addresses, and IPs.
Use Cases: Ensure URLs entered by users are valid.

##### 3. beautifulSoup4

Purpose: Parses HTML/XML content and makes web scraping easier.
Use Cases: Extracting specific data from web pages.

##### 4. lxml

Purpose: A powerful library for parsing XML and HTML with high performance.
Use Cases: Parsing large or complex HTML/XML documents.

##### 5. flask

Purpose: A lightweight web framework for building web applications
Use Cases: Create REST APIs, serve HTML pages, build dashboards

Install all the listed libraries by executing "pip install -r requirements.txt"

---

## Installation

### 1. Clone the repository:
   ```bash
   git clone https://github.com/dattu145/web_scraper.git
   cd web_scraper
   ```
### 2. Install Required Dependencies:
  ```bash
   pip install -r requirements.txt
  ```
### 3. Run the Flask App:
  ```bash
   python app.py
  ```
### 4. Open your browser and navigate to the localhost with port 5000:
   http://127.0.0.1:5000
