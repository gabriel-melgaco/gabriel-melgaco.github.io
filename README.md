Flask User Authentication, Profile Management, and Event Scheduling Application
A web application built with Flask that provides user registration, login, profile management, account settings functionality, and event scheduling. It leverages Flask-Login for user authentication and Peewee ORM with SQLite for database management.

Features
User Registration
Create an account with a unique username and email.
User Login and Logout
Authenticate and manage user sessions.
Protected Routes
Access restricted pages only when logged in.
Profile Management
Upload and update profile photos.
Update username and password.
Event Scheduling
Add Events: Users can create and add events to their calendar.
View Events: Users can view their events on a calendar interface.
Delete Events: Users can delete events from their calendar.
Commenting System
Add Comments: Users can add comments to posts.
View Comments: Comments are displayed below each post, aligned to the left.
Flash Messages
Receive feedback on actions like login, registration, profile updates, and event management.
Technologies Used
Backend
Flask: A lightweight WSGI web application framework.
Flask-Login: User session management for Flask.
Peewee: A simple and small ORM (Object-Relational Mapping) for Python.
SQLite: A lightweight disk-based database.
Frontend
HTML/CSS: For basic styling with Bootstrap classes for responsiveness.
FullCalendar: A JavaScript calendar library for event scheduling and management.
Installation and Setup
Clone the repository:

bash
Copiar código
git clone https://github.com/yourusername/yourrepository.git
Navigate to the project directory:

bash
Copiar código
cd yourrepository
Create a virtual environment and activate it:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash
Copiar código
pip install -r requirements.txt
Run the application:

bash
Copiar código
python app.py
Open your browser and go to http://127.0.0.1:5000 to use the application.

Configuration
Database: SQLite is used as the default database. You can change the database configuration in app.py if needed.
Session Management: Sessions are configured to be secure with HTTP-only and SameSite attributes.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Flask and Flask-Login for providing an easy-to-use framework and authentication management.
Peewee for a lightweight ORM.
FullCalendar for event management.
