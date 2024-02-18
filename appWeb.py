from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from transformers import pipeline
from langdetect import detect

summarizer_thai = pipeline("summarization", model="preechanon/mt5-base-thaisum-text-summarization")
summarizer_other = pipeline("summarization", model="Falconsai/text_summarization")

app = Flask(__name__)
def summarize_text(text):
    # Detect language using TextBlob
    language = detect(text)
    
    # Choose summarizer based on language
    if language == 'en':
       
        summary = summarizer_other(text)
    else:
        summary = summarizer_thai(text)
    
    return summary

@app.route('/')
def home():
    return render_template('indexWEB.php')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        url = request.form['url']
        # ดึงเนื้อหาจาก URL
        content = get_web_content(url)
        # สรุปเนื้อหาโดยใช้ AI
        summary = summarize_text(content)
        return render_template('resultWEB.php', summary=summary)

def get_web_content(url):
    # ดึงเนื้อหาจาก URL ด้วย BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # แยกเนื้อหาจาก HTML
    paragraphs = soup.find_all('p')
    content = ''
    for paragraph in paragraphs:
        content += paragraph.text + ' '
    return content

if __name__ == '__main__':
    app.run(debug=True)
