markdown
# Comprehensive Platform for Managing Energy Sector Licenses and Permits

This repository provides a simple Flask-based implementation of a platform designed to manage and visualize data from the 'Licenses and Permits in the Energy Sector 2025' dataset. The platform aims to enhance access, interactivity, and usability of the dataset by offering APIs, filtering options, and visualizations.

## Features

- **API for License Data**: Fetch information about energy sector licenses and permits.
- **Search and Filter**: Query licenses based on type and purpose.
- **Data Visualization**: Generate charts to visualize license distribution by type.
- **Real-Time Updates**: Ensure data is always up-to-date.

## Requirements

- Python 3.x
- Flask
- pandas

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/your-github-username/energy-sector-licenses.git
   cd energy-sector-licenses
   

2. Install dependencies:
   bash
   pip install -r requirements.txt
   

3. Place the dataset (`Licence_Category.csv`) in the root directory of the project.

4. Run the application:
   bash
   python app.py
   

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## API Endpoints

### 1. Fetch all licenses

**GET /api/licenses**

**Query Parameters:**
- `type` (optional): Filter licenses by type (e.g., "Electricity", "Water").
- `purpose` (optional): Filter licenses by purpose (e.g., "Internal Consumption").

**Response:**

[
  {
    "ID": 1,
    "Type": "Electricity",
    "Purpose": "Generation",
    ...
  },
  ...
]


### 2. Fetch license by ID

**GET /api/license/:license_id**

**Path Parameters:**
- `license_id` (required): The ID of the license.

**Response:**

{
  "ID": 1,
  "Type": "Electricity",
  "Purpose": "Generation",
  ...
}


### 3. Visualize licenses by type

**GET /api/licenses/visualize**

**Response:**

{
  "Electricity": 10,
  "Water": 5,
  ...
}


## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For inquiries, please contact:
- **Name**: Abu Dhabi Department of Energy
- **Email**: energy@abudhabi.gov.ae
