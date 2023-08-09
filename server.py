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

@app.route('/injest', methods=['POST'])
def injest():
    req = request.get_json()
    inputPath = req['inputPath']
    outputPath = req['outputPath']
    print('Creating vector db using docs in path: ',inputPath)
    create_vector_db(inputPath, outputPath)
    print('Vector db indexes generated in: ',outputPath)



if __name__ == '__main__':
    app.run()

# greet on / route


@app.route('/')
def index():
    return "Hello, World!"
