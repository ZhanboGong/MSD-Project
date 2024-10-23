from flask import Flask, jsonify
from api.doctor_api import get_patient_record, edit_patient_record

app = Flask(__name__)

@app.route('/api/patient/<int:id>', methods=['GET'])
def get_patient(id):
    return get_patient_record(id)

@app.route('/api/patient/<int:id>', methods=['POST'])
def edit_patient(id):
    return edit_patient_record(id)

if __name__ == '__main__':
    app.run(debug=True)
