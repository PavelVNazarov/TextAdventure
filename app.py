# app.py
# python app.py
from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Путь к папке с JSON файлами
DATA_FOLDER = 'data'

@app.route('/')
def index():
    # Получаем список файлов JSON
    books = [f for f in os.listdir(DATA_FOLDER) if f.endswith('.json')]
    return render_template('index.html', books=books)

@app.route('/book/<filename>')
def book(filename):
    with open(os.path.join(DATA_FOLDER, filename), encoding='utf-8-sig') as f:
        data = json.load(f)
    return render_template('book.html', book=data)

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/paragraph/<filename>/<int:paragraph_number>')
def paragraph(filename, paragraph_number):
    file_path = os.path.join(DATA_FOLDER, filename)
    with open(file_path, encoding='utf-8-sig') as f:
        data = json.load(f)
    paragraphs = data['paragraphs']
    current_paragraph = next((p for p in paragraphs if p['number'] == paragraph_number), None)
    return render_template('paragraph.html', book=data, paragraph=current_paragraph)

if __name__ == '__main__':
    app.run(debug=True)

