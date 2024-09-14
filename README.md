Flask User Authentication, Profile Management, and Event Scheduling Application

A web application built with Flask that provides user registration, login, profile management, account settings functionality, and event scheduling. It leverages Flask-Login for user authentication and Peewee ORM with SQLite for database management.

 *Features*

- User Registration: Create an account with a unique username and email.
- User Login and Logout: Authenticate and manage user sessions.
- Protected Routes: Access restricted pages only when logged in.
- Profile Management:
- Upload and update profile photos.
- Update username and password.
- Event Scheduling:
- Add Events: Users can create and add events to their calendar.
- View Events: Users can view their events on a calendar interface.
- Delete Events: Users can delete events from their calendar.
- Flash Messages: Receive feedback on actions like login, registration, profile updates, and event management.

*Technologies Used*

-> Backend:
Flask – A lightweight WSGI web application framework.
Flask-Login – User session management for Flask.
Peewee – A simple and small ORM (Object-Relational Mapping) for Python.
SQLite – A lightweight disk-based database.

-> Frontend:
HTML/CSS (with Bootstrap classes for styling)
FullCalendar – A JavaScript calendar library for event scheduling and management.
