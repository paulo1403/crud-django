# CRUD Project with Django

This is a comprehensive CRUD (Create, Read, Update, Delete) application built with Django. It allows users to manage items with name, description, file attachments, tags, and more.

## Features

### Core Functionality

- List all items with advanced pagination
- Create new items with rich metadata
- View detailed item information
- Edit existing items
- Delete items

### Advanced Features

- **User Authentication System**: Registration, login, and profile editing
- **File Upload**: Attach images and documents to items
- **Tagging System**: Categorize items with tags for better organization
- **Search and Filtering**: Find items by text, creator, file type, or tags
- **Comment System**: Collaborate through comments on items
- **Change History**: Track all modifications with detailed audit trail
- **Responsive UI**: Modern Bootstrap interface that works on all devices

## Technologies Used

- **Backend**: Python 3.x, Django 4.x
- **Frontend**: Bootstrap 5, JavaScript
- **Database**: SQLite (default), easily configurable for PostgreSQL, MySQL, etc.
- **File Storage**: Django's FileField for handling uploaded files
- **UI Components**: Bootstrap Icons, responsive layout components
- **Themes**: Light/Dark mode toggle with persistent preferences

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

5. **Create a superuser** (optional, for admin access):

   ```bash
   python3 manage.py createsuperuser
   ```

6. **Start the development server**:

   ```bash
   python3 manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage Guide

### User Authentication

- Register a new account or log in with existing credentials
- Edit your profile information including name and email
- Staff users have access to the change log history

### Managing Items

- **List View**: See all items with pagination, search and filtering options
- **Detail View**: Click on an item name or "View" button to see full details
- **Item Creation**: Add new items with name, description, tags, and file attachment
- **Item Editing**: Modify existing items including their attached files and tags
- **Item Deletion**: Remove items no longer needed

### Working with Tags

- Create new tags when adding or editing items
- Filter items by tag using the dropdown or by clicking on a tag badge
- Tags help organize and categorize items for easy discovery

### Comments System

- Add comments on item detail pages
- See all comments with their authors and timestamps
- Foster collaboration through discussion

## Project Structure

- `crud_app/`: Contains the application logic
  - `models.py`: Data models (Item, Tag, Comment, ChangeLog)
  - `views.py`: View functions handling user requests
  - `urls.py`: URL routing configuration
  - `forms.py`: Form definitions for data validation
  - `templates/`: HTML templates for rendering pages
  - `static/`: Static files (JS, CSS, images)
  - `migrations/`: Database migration files
- `crud_project/`: Contains the project settings and configuration
- `media/`: Stores user-uploaded files
- `db.sqlite3`: SQLite database file
- `venv/`: Virtual environment (not included in the repository)

## Features Details

### File Upload System

- Support for various file types including documents and images
- Automatic detection and display of image files vs. regular files
- Option to remove attached files when editing items

### Searching & Filtering

- Text search across item names and descriptions
- Filter by creator/user
- Filter by file type (with files, with images, no files)
- Filter by tags

### Pagination System

- Efficiently handles large datasets with page navigation
- Shows current viewing range and total item count
- Maintains search parameters and filters across pages

### Change Tracking

- Complete history of all item changes
- Records create, update, and delete operations
- Preserves item information even after deletion
- Staff users can access complete change log

### Theme Switching

- Toggle between light and dark themes
- User preference saved between sessions
- Automatic theme switching based on saved preference

## Notes

- Make sure to activate the virtual environment before running the project
- The project uses Bootstrap 5 for responsive, modern styling
- For file uploads to work properly, ensure the media directory is writable
- For the best experience, use a modern browser that supports Bootstrap 5

## License

This project is open-source and available under the MIT License.
