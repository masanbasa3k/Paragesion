from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

def question_answering(input_data, model_name="deepset/roberta-base-squad2"):
    # Load model & tokenizer
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Get predictions
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    res = nlp(input_data)

    return res['answer']

if __name__ == "__main__":
    # Example usage:
    input_data = {
        'question': 'What is his name',
        'context': 'His name is John Doe. He lives in New York. He is a software engineer.'
    }
    response = question_answering(input_data)
    print(response)
