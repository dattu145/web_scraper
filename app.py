import os
from flask import Flask, render_template, request
from web_scrapper import extract_html, extract_text, extract_headings, extract_links, extract_by_tag

app = Flask(__name__, template_folder=os.getcwd())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    choice = request.form['choice']
    tagn = request.form.get('tagn')

    if choice == "1":
        result = extract_html(url)
    elif choice == "2":
        result = extract_text(url)
    elif choice == "3":
        result = extract_headings(url)
    elif choice == "4":
        result = extract_links(url)
    elif choice == "5" and tagn:
        result = extract_by_tag(url, tagn)
    else:
        result = "Invalid choice or missing tag name."

    return result  

if __name__ == '__main__':
    app.run(debug=True)
