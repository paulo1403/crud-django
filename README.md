# CRUD Project with Django

This is a simple CRUD (Create, Read, Update, Delete) application built with Django. It allows users to manage items with a name and description.

## Features

- List all items
- Add new items
- Edit existing items
- Delete items

## Requirements

- Python 3.x
- Django 4.x

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install django
   ```

4. **Run migrations**:

   ```bash
   python3 manage.py migrate
   ```

5. **Start the development server**:

   ```bash
   python3 manage.py runserver
   ```

6. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`.

## Project Structure

- `crud_app/`: Contains the application logic (models, views, templates, etc.).
- `crud_project/`: Contains the project settings and configuration.
- `db.sqlite3`: SQLite database file.
- `venv/`: Virtual environment (not included in the repository).

## Notes

- Make sure to activate the virtual environment before running the project.
- The project uses Bulma CSS for styling.

## License

This project is open-source and available under the MIT License.
