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

- **User Authentication System**: Registration, login, password reset, and profile editing
- **File Upload**: Attach images and documents to items
- **Tagging System**: Categorize items with tags for better organization
- **Search and Filtering**: Find items by text, creator, file type, or tags
- **Comment System**: Collaborate through comments on items
- **Change History**: Track all modifications with detailed audit trail
- **Responsive UI**: Modern Bootstrap interface that works on all devices
- **Kanban Board**: Visual task management with drag-and-drop functionality
- **Favorites System**: Bookmark items for quick access
- **Password Reset**: Secure password recovery via email

## Technologies Used

- **Backend**: Python 3.x, Django 4.x
- **Frontend**: Bootstrap 5, JavaScript
- **Database**: SQLite (default), easily configurable for PostgreSQL, MySQL, etc.
- **File Storage**: Django's FileField for handling uploaded files
- **UI Components**: Bootstrap Icons, responsive layout components
- **Themes**: Light/Dark mode toggle with persistent preferences
- **Interactive UI**: Drag-and-drop functionality, tooltips, form validation

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
- Reset forgotten passwords through secure email verification
- Edit your profile information including name and email
- Staff users have access to the change log history

### Managing Items

- **List View**: See all items with pagination, search and filtering options
- **Detail View**: Click on an item name or "View" button to see full details
- **Kanban View**: Visualize and organize items by status (To Do, In Progress, Done)
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

### Kanban Board

- Drag and drop items between status columns (To Do, In Progress, Done)
- Visual indication of item status with color-coded columns
- Items maintain their tags, descriptions, and other metadata across status changes
- Real-time status updates without page reload
- Favorite items are highlighted for quick identification

### Favorites System

- Mark items as favorites for quick access
- Filter to see only favorite items
- Visual highlighting of favorite items in all views
- Toggle favorite status with a single click

### Password Reset System

- Request password reset via registered email
- Receive secure time-limited reset link
- Create and confirm new password with security requirements
- Confirmation on successful password change

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
- Tracks status changes in Kanban workflow

### Theme Switching

- Toggle between light and dark themes
- User preference saved between sessions
- Automatic theme detection based on system preferences
- Consistent styling across all components in both themes

### User Interface Improvements

- Icon-only actions with tooltips for cleaner interface
- Improved form validation with visual feedback
- Enhanced login and registration screens
- Responsive design that adapts to mobile, tablet, and desktop views
- Consistent visual language across the application

## Notes

- Make sure to activate the virtual environment before running the project
- The project uses Bootstrap 5 for responsive, modern styling
- For file uploads to work properly, ensure the media directory is writable
- For the best experience, use a modern browser that supports Bootstrap 5
- For password reset emails in production, configure a proper email backend

## License

This project is open-source and available under the MIT License.
