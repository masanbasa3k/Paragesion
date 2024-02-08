from flask import Blueprint, render_template, request
import sys
sys.path.append("paragesion")

from take_data import concatenate_paragraphs_from_urls

views = Blueprint(__name__, "views")
input_data = None

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/process_input', methods=['POST'])
def process_input():
    input = request.form['input']
    # Do something with the input data here
    input_paragraph = concatenate_paragraphs_from_urls(input)
    return f'Input received: {input_paragraph}'

@views.route('/process_question', methods=['POST'])
def process_question():
    question = request.form['questionInput']
    # Burada alınan soruyu kullanarak istediğiniz işlemi gerçekleştirebilirsiniz.
    # Örneğin, bu soruyu bir veritabanına kaydedebilir veya başka bir uygulamaya gönderebilirsiniz.
    print("Received question:", question)
    return 'Question received: ' + question