import csv
from flask import Flask, jsonify, request
from flask_cors import CORS
# from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
CORS(app)
# api = Api(app)

@app.route('/docs_info/<int:doc_id>', methods=['GET'])
def get_sim_docs(doc_id):
    # Open CSV file
    with open('similarities.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check if the row corresponds to the requested doc_id
            if int(row['Doc ID']) == doc_id:
                # If found, return the similarity percentage as JSON response
                sim1 = float(row['Sim1'])*100
                sim2 = float(row['Sim2'])*100
                sim3 = float(row['Sim3'])*100
                sim4 = float(row['Sim4'])*100
                return jsonify({ 'd': [row['D1'],  row['D2'], row['D3'], row['D4']], 'sim': [sim1, sim2, sim3, sim4] })
    
    # If not found, return a 404 error
    return jsonify({'error': 'doc not found'}), 404
    
# api.add_resource(TestClass, "/next")    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
