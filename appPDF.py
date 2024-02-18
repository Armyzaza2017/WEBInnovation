from flask import Flask, render_template, request
import PyPDF2
from transformers import pipeline
from langdetect import detect

app = Flask(__name__)

# Load the summarization pipeline
summarizer_thai = pipeline("summarization", model="preechanon/mt5-base-thaisum-text-summarization")
summarizer_other = pipeline("summarization", model="Falconsai/text_summarization")
def summarize_text(text):
    # Detect language using TextBlob
    language = detect(text)
    
    # Choose summarizer based on language
    if language == 'en':
       
        summary = summarizer_other(text)
    else:
        summary = summarizer_thai(text)
    
    return summary
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

@app.route('/')
def home():
    return render_template('indexPDF.php')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.pdf'):
            text = extract_text_from_pdf(file)
            summary = summarize_text(text)
            return render_template('resultPDF.php', summary=summary)
        else:
            return "Please upload a .pdf file."

if __name__ == '__main__':
    app.run(debug=True)
