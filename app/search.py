from flask import Flask, render_template, request
import re

app = Flask(__name__)

def count_complete_word(paragraph, word):
    pattern = r'\b' + re.escape(word) + r'\b'
    matches = re.findall(pattern, paragraph, re.IGNORECASE)
    return len(matches)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        paragraph = request.form['paragraph']
        word_to_count = request.form['word']
        result = count_complete_word(paragraph, word_to_count)
        return render_template('index.html', result=result, paragraph=paragraph, word=word_to_count)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)