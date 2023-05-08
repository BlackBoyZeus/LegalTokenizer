from flask import Flask, render_template, request
from legal_tokenizer import LegalTokenizer

app = Flask(__name__)
tokenizer = LegalTokenizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tokenize', methods=['POST'])
def tokenize():
    text = request.form['text']
    tokens = tokenizer.tokenize(text)
    return render_template('tokenize.html', text=text, tokens=tokens)

if __name__ == '__main__':
    app.run(debug=True)
