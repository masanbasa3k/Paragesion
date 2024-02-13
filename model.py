from transformers import pipeline
question_answerer = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')

def question_answering(input_data):
    
    question, context = input_data['question'], input_data['context']

    result = question_answerer(
        question=question,
        context=context)

    return result['answer']

if __name__ == "__main__":
    # Example usage:
    input_data = {
        'question': 'What is his name',
        'context': 'His name is John Doe. He lives in New York. He is a software engineer.'
    }
    response = question_answering(input_data)
    print(response)
