import os
import qna
import json
import extractText
import generateQuestionAnswer
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("aboutus.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/output')
def output():
    return render_template("output.html")

@app.route('/error')
def error():
    return render_template("error.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            f = request.files['file']
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)
            extention_type = file_path
            extention = extention_type.split('.')
            print(extention, extention[-1])
            print(type(extention[-1]))

            text = ""
            if extention[-1] in ["jpg","jpeg","png","JPG", "PNG", "JPEG"]:
                print("image")
                text = extractText.extractTextFromImg(file_path)
                print(text)
            elif extention[-1] in ["pdf","PDF"]:
                print("pdf")
                text = extractText.extractTextFromPdf(file_path)
                print(text)
            text = text.lower()

            QandA = qna.generateQnA(text)
            print("app.py", QandA)
            QandA_dict = json.loads(QandA)
        except Exception as e: 
            print(e)
            return render_template('error.html')
        
        
            # questions = generateQuestionAnswer.generateQuestions(text)
            # answers = generateQuestionAnswer.generateAnswers(text,questions)

            # return [questions, answers]
            # return QandA
        return render_template('output.html', QandA = QandA_dict)
       


if __name__ == '__main__':
    app.run(debug=True)