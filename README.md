
    <h1>Flask User Authentication, Profile Management, and Event Scheduling Application</h1>
    <p>A web application built with Flask that provides user registration, login, profile management, account settings functionality, and event scheduling. It leverages Flask-Login for user authentication and Peewee ORM with SQLite for database management.</p>

    <h2>Features</h2>
    <h3>User Registration</h3>
    <ul>
        <li>Create an account with a unique username and email.</li>
    </ul>

    <h3>User Login and Logout</h3>
    <ul>
        <li>Authenticate and manage user sessions.</li>
    </ul>

    <h3>Protected Routes</h3>
    <ul>
        <li>Access restricted pages only when logged in.</li>
    </ul>

    <h3>Profile Management</h3>
    <ul>
        <li>Upload and update profile photos.</li>
        <li>Update username and password.</li>
    </ul>

    <h3>Event Scheduling</h3>
    <ul>
        <li><strong>Add Events:</strong> Users can create and add events to their calendar.</li>
        <li><strong>View Events:</strong> Users can view their events on a calendar interface.</li>
        <li><strong>Delete Events:</strong> Users can delete events from their calendar.</li>
    </ul>

    <h3>Commenting System</h3>
    <ul>
        <li><strong>Add Comments:</strong> Users can add comments to posts.</li>
        <li><strong>View Comments:</strong> Comments are displayed below each post, aligned to the left.</li>
    </ul>

    <h3>Flash Messages</h3>
    <ul>
        <li>Receive feedback on actions like login, registration, profile updates, and event management.</li>
    </ul>

    <h2>Technologies Used</h2>
    <h3>Backend</h3>
    <ul>
        <li><strong>Flask:</strong> A lightweight WSGI web application framework.</li>
        <li><strong>Flask-Login:</strong> User session management for Flask.</li>
        <li><strong>Peewee:</strong> A simple and small ORM (Object-Relational Mapping) for Python.</li>
        <li><strong>SQLite:</strong> A lightweight disk-based database.</li>
    </ul>

    <h3>Frontend</h3>
    <ul>
        <li><strong>HTML/CSS:</strong> For basic styling with Bootstrap classes for responsiveness.</li>
        <li><strong>FullCalendar:</strong> A JavaScript calendar library for event scheduling and management.</li>
    </ul>

    <h2>Installation and Setup</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/yourusername/yourrepository.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd yourrepository</code></pre>
        </li>
        <li>Create a virtual environment and activate it:
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
        </li>
        <li>Install the required dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Run the application:
            <pre><code>python app.py</code></pre>
        </li>
        <li>Open your browser and go to <code>http://127.0.0.1:5000</code> to use the application.</li>
    </ol>

    <h2>Configuration</h2>
    <ul>
        <li><strong>Database:</strong> SQLite is used as the default database. You can change the database configuration in <code>app.py</code> if needed.</li>
        <li><strong>Session Management:</strong> Sessions are configured to be secure with HTTP-only and SameSite attributes.</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Acknowledgments</h2>
    <ul>
        <li>Flask and Flask-Login for providing an easy-to-use framework and authentication management.</li>
        <li>Peewee for a lightweight ORM.</li>
        <li>FullCalendar for event management.</li>
    </ul>
</body>
</html>
