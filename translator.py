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
    <title>Multi-language Translator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f4f8;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            max-width: 600px;
            width: 100%;
            text-align: center;
        }
        h1 {
            color: #2c3e50;
        }
        label, select, textarea, input[type="submit"] {
            font-size: 16px;
            margin-top: 10px;
        }
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            resize: vertical;
        }
        select, input[type="submit"] {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background-color: #3498db;
            color: white;
            cursor: pointer;
        }
        select:hover, input[type="submit"]:hover {
            background-color: #2980b9;
        }
        p {
            font-size: 18px;
            color: #333;
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Multi-language Translator</h1>
        <form method="POST" action="/">
            <label for="text">Enter text to translate:</label><br><br>
            <textarea id="text" name="text" rows="6" placeholder="Enter text here..."></textarea><br><br>

            <label for="language">Select target language:</label><br><br>
            <select id="language" name="language">
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
                <option value="de">German</option>
                <option value="ja">Japanese</option>
                <option value="ko">Korean</option>
                <option value="ru">Russian</option>
                <option value="ar">Arabic</option>
                <option value="pt">Portuguese</option>
                <option value="it">Italian</option>
                <option value="hi">Hindi</option>
                <!-- Add more language options as needed -->
            </select><br><br>

            <input type="submit" value="Translate">
        </form>

        <h2>Translated Text :</h2>
        <p>{{ translation }}</p>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def translate():
    translation = ""
    if request.method == 'POST':
        text = request.form['text']
        target_language = request.form['language']
        translation = GoogleTranslator(source='auto', target=target_language).translate(text)
    
    # Return the HTML with the translation result
    return html_template.replace('{{ translation }}', translation if translation else '')

if __name__ == '__main__':
    app.run(debug=True)
