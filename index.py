python
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load dataset
DATA_FILE_PATH = 'Licence_Category.csv'
data = pd.read_csv(DATA_FILE_PATH)

@app.route('/api/licenses', methods=['GET'])
def get_licenses():
    """
    API Endpoint to fetch license data with optional filtering.
    Query Parameters:
    - type: Filter licenses by type (e.g., "Electricity", "Water")
    - purpose: Filter licenses by purpose (e.g., "Internal Consumption")

    Returns:
    - JSON response containing filtered license data.
    """
    license_type = request.args.get('type')
    purpose = request.args.get('purpose')

    filtered_data = data

    if license_type:
        filtered_data = filtered_data[filtered_data['Type'].str.contains(license_type, case=False)]

    if purpose:
        filtered_data = filtered_data[filtered_data['Purpose'].str.contains(purpose, case=False)]

    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('/api/license/<int:license_id>', methods=['GET'])
def get_license_by_id(license_id):
    """
    API Endpoint to fetch license data by ID.
    :param license_id: ID of the license

    Returns:
    - JSON response containing the license details.
    """
    license_data = data[data['ID'] == license_id]

    if license_data.empty:
        return jsonify({"error": "License not found"}), 404

    return jsonify(license_data.to_dict(orient='records')[0])

@app.route('/api/licenses/visualize', methods=['GET'])
def visualize_licenses():
    """
    API Endpoint to provide a visualization of licenses by type.

    Returns:
    - Chart data in JSON format.
    """
    chart_data = data['Type'].value_counts().to_dict()
    return jsonify(chart_data)

if __name__ == '__main__':
    app.run(debug=True)
