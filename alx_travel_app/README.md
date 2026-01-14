# ALX Travel App (Project 0x00)

A robust backend API built with Django and Django REST Framework for a travel marketplace. This project manages property listings, user bookings, and reviews, featuring automated documentation and asynchronous task handling.



## 🚀 Features

- **Relational Data Modeling:** Structured schema for Listings, Bookings, and Reviews with UUID primary keys.
- **RESTful API:** Clean endpoints for CRUD operations powered by ViewSets and Routers.
- **Automated Documentation:** Interactive API exploration via Swagger UI and ReDoc.
- **Database Seeding:** Custom management commands to populate the environment with sample data.
- **Background Tasks:** Ready for Celery & RabbitMQ integration for asynchronous processing.

## 🛠 Tech Stack

- **Framework:** [Django 5.x](https://www.djangoproject.com/)
- **API Toolkit:** [Django REST Framework](https://www.django-rest-framework.org/)
- **Database:** MySQL
- **Documentation:** [drf-yasg](https://github.com/axnsan12/drf-yasg) (OpenAPI 2.0)
- **Environment Management:** django-environ

## 📂 Project Structure

```text
alx_travel_app_0x00/
├── alx_travel_app/         # Core configuration
│   ├── settings.py         # App & DB settings
│   └── urls.py             # Root URL routing (Swagger)
├── listings/               # Core application logic
│   ├── management/         # Custom management commands (Seeders)
│   ├── models.py           # Listing, Booking, and Review models
│   ├── serializers.py      # Data transformation logic
│   └── views.py            # API ViewSets
└── .env                    # Environment variables (Secrets)

⚙️ Installation & Setup
1. Clone the Repository
Bash

git clone [https://github.com/yourusername/alx_travel_app_0x00.git](https://github.com/yourusername/alx_travel_app_0x00.git)
cd alx_travel_app_0x00
2. Configure Environment Variables
Create a .env file in the root directory:

Code snippet

SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=alx_travel_app
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=3306
CORS_ALLOWED_ORIGINS=http://localhost:3000
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Database Migrations & Seeding
Bash

python manage.py makemigrations
python manage.py migrate
python manage.py seed

📖 API Documentation
Once the server is running (python manage.py runserver), you can access the interactive documentation at:

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/
