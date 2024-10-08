from flask import Flask, request
from deep_translator import GoogleTranslator


app = Flask(__name__)

# HTML template embedded in the Python code
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hindi to English Translator</title>
</head>
<body>
    <h1>Hindi to English Translator</h1>
    <form method="POST" action="/">
        <label for="hindi_text">Enter Hindi text:</label><br><br>
        <textarea id="hindi_text" name="hindi_text" rows="10" cols="100"  placeholder="Enter Hindi text here..."></textarea><br><br>

        <input type="submit" value="Translate">
    </form>

    
        <h2>Translated Text (English) :</h2>
        <p>{{ translation }}</p>
    
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def translate():
    translation = ""
    if request.method == 'POST':
        hindi_text = request.form['hindi_text']
        translation = GoogleTranslator(source='hi', target='en').translate(hindi_text)
    
    # Return the HTML with the translation result
    return html_template.replace('{{ translation }}', translation if translation else '')

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000 after run the code hit this in to your browser url sectioN