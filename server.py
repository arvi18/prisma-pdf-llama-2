from flask import Flask, request, jsonify
import langchain
from model import qa_bot, final_result

app = Flask(__name__)

# Load the chatbot components
qa_bot = qa_bot()


@app.route('/chat', methods=['POST'])
def chat():
    query = request.json['query']
    print(query)

    response = final_result(query)
    # return jsonify({'response': response})
    return response


if __name__ == '__main__':
    app.run()

# greet on / route


@app.route('/')
def index():
    return "Hello, World!"
