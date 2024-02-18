from flask import Flask, render_template, request
from langdetect import detect
from transformers import pipeline

app = Flask(__name__)

# Load the summarization pipelines
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

@app.route('/')
def home():
    return render_template('indexTXT.php')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.txt'):
            text = file.read().decode('utf-8')
            summary = summarize_text(text)
            return render_template('resultTXT.php', summary=summary)
        else:
            return "Please upload a .txt file."

if __name__ == '__main__':
    app.run(debug=True)
