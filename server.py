"""
This module contains a Flask server that provides an API endpoint for a chatbot. The chatbot is implemented using the
`qa_bot` and `final_result` functions from the `model` module. The server listens for POST requests to the `/chat` endpoint
and expects a JSON payload with a `query` field. The server responds with a JSON payload containing the original query,
the chatbot's response, and a message indicating that no source documents are available. The server can be started by
running this module directly.
"""

from flask import Flask, request
from model import qa_bot, final_result
from ingest import create_vector_db

app = Flask(__name__)

# Load the chatbot components
qa_bot = qa_bot()


@app.route('/chat', methods=['POST'])
def chat():
    query = request.json['query']
    print(query)

    response = final_result(query)
    response["source_documents"] = "No source documents available"
    return response


@app.route('/ingest', methods=['POST'])
def injest():
    req = request.get_json()
    inputPath = req['inputPath']
    outputPath = req['outputPath']
    print('Creating vector db using docs in path: ', inputPath)
    create_vector_db(inputPath, outputPath)
    print('Vector db indexes generated in: ', outputPath)


if __name__ == '__main__':
    app.run()

# sample request
# {
#   "query": "What is the capital of France?"
# }

# sample response
# {
#   "query": "What is the capital of France?",
#   "result": "Tardive dyskinesia, often known as “Bartholin’s cyst,” can be a severe side effect of certain antipsychotic medications. The condition occurs when glands (small ovarian-like organs) in the vulva become enlarged and then painful and uncomfortable to the patient.\n\nThe Bartholin’s gland cysts are commonly found in women of reproductive age, developing in approximately 2% of all women. The condition is caused by a blockage within the ovarian-like organs. These cysts and abscess-es may show up on mammograms or ultrasounds for patients who have this condition.\n\nTreatment\nIf you are diagnosed with Bartholin’s gland cysts, your doctor will likely prescribe antibiotics to treat the infection. This medication is usually taken orally and can be taken alongside other medications if necessary. If the antibiotic does not work, surgery may be required.\n\nPotential Risk Factors\nThe most common risk factor for developing a Bartholin’s gland cyst is having",
#   "source_documents": ""
# }
