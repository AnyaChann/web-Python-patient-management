# Patient Management System

This is a simple Patient Management System built using Flask and SQLite. The system allows you to add, edit, delete, and view patient records. It also includes functionality to add example data and reset the ID sequence when the table is empty.

## Features

- Add new patient records
- Edit existing patient records
- Delete patient records
- Delete multiple patient records
- Add example data
- Reset ID sequence when the table is empty
- Sort patient records by column

## Prerequisites

- Python 3.x
- Flask
- SQLite

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/patient-management-system.git
    cd patient-management-system
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Project

1. Ensure you are in the project directory and the virtual environment is activated.

2. Run the Flask application:
    ```sh
    flask run
    ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the Patient Management System.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing static files like CSS and JavaScript.
- `patients.db`: SQLite database file.

## Usage

### Adding a New Patient

1. Click on the "Add New Patient" button.
2. Fill in the patient details and click "Submit".

### Editing a Patient

1. Click on the "Edit" button next to the patient you want to edit.
2. Update the patient details and click "Submit".

### Deleting a Patient

1. Click on the "Delete" button next to the patient you want to delete.
2. Confirm the deletion.

### Deleting Multiple Patients

1. Select the patients you want to delete by clicking the checkboxes.
2. Click on the "Delete Selected" button.
3. Confirm the deletion.

### Adding Example Data

1. Click on the "Add Example Data" button to populate the database with example patient records.

### Resetting ID Sequence

The ID sequence is automatically reset when the table is empty.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.