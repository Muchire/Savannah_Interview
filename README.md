<!-- Customers Order API

This is a API that manages customer orders and sends an SMS when an order is made.
It is built using Django and Django REST Framework, it allows CRUD operations fro customers and orders.

Features
User authentication using Google OpenID Connect
SMS notification using Africa's Talking
PostgreSQL database for data storage

Setup and Installation
1. Clone the repository
  git clone https://github.com/Muchire/Savannah_Interview.git
  cd Savannah_Interview

2. Create a Virtual Environment
   python -m venv venv
   source venv/bin/activate

3.Install Dependencies
   pip install -r requirements.txt

4.Set uo the environment variables. Create .env file in your project root and enter the details below as provided by the different services

SECRET_KEY=<your-secret-key>
DB_NAME=<your-database-name>
DB_USER=<your-database-user>
DB_PASSWORD=<your-database-password>
DB_HOST=localhost
DB_PORT=5432
AFRICASTALKING_USERNAME=<your-africastalking-username>
AFRICASTALKING_API_KEY=<your-africastalking-api-key>
GOOGLE_CLIENT_ID=<your-google-client-id>
GOOGLE_CLIENT_SECRET=<your-google-client-secret>

5. Setup the Database 
  python manage.py makemigrations
  python manage.py migrate

6. Run the Server
   python manage.py runserver

Usage

The API endpoints are available at http://localhost:8000/api/

Authentication is handled via Google OpenID Connect.

When an order is made, an SMS notification is sent to the user's phone number using Africa's Talking, this is seen from the logs.

The application has been tested using Postman.

Testing

Run unit tests with coverage
  python manage.py test

Contributing

Contributions are welcome. Please create a pull request with your changes.

License

This project is licensed under the MIT License. -->