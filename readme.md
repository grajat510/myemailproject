# MyEmailProject

MyEmailProject is a Django-based web application with email sending capabilities, similar to Gmail. The project uses MongoDB for data storage and integrates OpenAI's GPT-3 for composing and replying to emails.

## Prerequisites

- Python 3.11
- Django 3.2
- MongoDB
- A MongoDB Compass installation for database management
- An OpenAI API key

## Project Structure
myemailproject/
├── emailapp/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ ├── views.py
│ ├── templates/
│ │ └── emailapp/
│ │ ├── compose.html
│ │ ├── generate_email.html
│ │ ├── inbox.html
│ │ ├── login.html
│ │ └── register.html
├── myemailproject/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── .env
├── create_mongo_user.py
├── init_mongodb.py
├── manage.py
├── requirements.txt
├── test_mongodb_connection.py
└── venv/
├── Scripts/
├── Lib/
└── ...



## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/yourusername/myemailproject.git
cd myemailproject

2. Create a Virtual Environment

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Environment Variables
Create a .env file in the root directory with the following content.

SECRET_KEY=your_secret_key
DEBUG=True
MONGO_DB_NAME=myemailproject
MONGO_DB_HOST=localhost
MONGO_DB_PORT=27017
MONGO_DB_USERNAME=myusername
MONGO_DB_PASSWORD=mypassword
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
OPENAI_API_KEY=your_openai_api_key
MONGO_URI=mongodb://myusername:mypassword@localhost:27017/myemailproject

5. Initialize MongoDB

python test_mongodb_connection.py
python create_mongo_user.py
python init_mongodb.py

6. Make Migrations and Migrate

python manage.py makemigrations
python manage.py migrate

7. Create a Superuser

python manage.py createsuperuser

8. Run the Server

python manage.py runserver

## Usage
Navigate to http://127.0.0.1:8000/login/ to log in.
Use the superuser credentials to access the admin interface at http://127.0.0.1:8000/admin/.