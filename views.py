from flask import Blueprint, render_template, request

from take_data import concatenate_paragraphs_from_urls

views = Blueprint(__name__, "views")
input_data = None
status = ''

@views.route('/', methods=['POST','GET'])
def home():
    input = request.form['input']
    input_paragraph = concatenate_paragraphs_from_urls(input)
    if input_paragraph != "":
        return render_template('index.html', status='basariii', input_paragraph=input_paragraph)
    else:
        return render_template('index.html', status='data not taken', input_paragraph=input_paragraph)

@views.route('/', methods=['POST'])
def process_question():
    question = request.form['questionInput']
    # Burada alınan soruyu kullanarak istediğiniz işlemi gerçekleştirebilirsiniz.
    # Örneğin, bu soruyu bir veritabanına kaydedebilir veya başka bir uygulamaya gönderebilirsiniz.
    print("Received question:", question)
    return 'Question received: ' + question