from flask import Flask, request, render_template_string
from textSimilarity import *

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text1 = request.form.get('text1')
        text2 = request.form.get('text2')
        
        compObj = TextCompare(text1, text2)
        score = compObj.run()
    else:
        text1 = ''
        text2 = ''
        score = ''
    return render_template_string('''
        <form action="/" method="POST">
            <p>Text 1: <textarea name="text1" id="text1" wrap="soft" value="{{ text1 }}"></textarea> </p>
            <p>Text 2: <textarea name="text2" id="text2" wrap="soft" value="{{ text2 }}"></textarea> </p>
            <input type="submit" value="Compare">
            <p>Result: <input type="number" name="score" id="score" value="{{ score }}"></p>
        </form>''', text1=text1, text2=text2, score=score)

if __name__ == '__main__':
    app.run()
