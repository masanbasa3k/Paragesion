from flask import Blueprint, render_template, request

from take_data import concatenate_paragraphs_from_urls
from model import question_answering

views = Blueprint(__name__, "views")

@views.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        input_data = request.form.get('input', '')  # Formdan veriyi al
        input_paragraph = concatenate_paragraphs_from_urls(input_data)  # Veriyi işle
        if input_paragraph:
            return render_template('index.html', input_paragraph=input_paragraph)
        else:
            return render_template('index.html', input_paragraph='Data not taken')
    else:
        return render_template('index.html', input_paragraph='')


@views.route('/ask', methods=['POST','GET'])
def ask_question():
    input_paragraph = request.form.get('input_paragraph', '')  # Formdan input_paragraph verisini al
    question = request.form.get('questionInput', '')
    answer = 'answer will be here...'
    input_data = {
        'question': question,
        'context': input_paragraph
    }
    if input_paragraph and question:
        answer = question_answering(input_data)
    return render_template('index.html', input_paragraph=input_paragraph, question=question, answer=answer)
