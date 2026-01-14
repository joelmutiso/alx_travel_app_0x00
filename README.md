# <p align="center">✈️ ALX Travel App (Project 0x00)</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/DRF-REST%20API-ff1709?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Celery-Ready-37814A?style=for-the-badge&logo=celery&logoColor=white" />
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,15,18&height=150&section=header&text=Professional%20Travel%20Marketplace&fontSize=35&animation=fadeIn&fontAlignY=38&fontColor=fff" />
</p>

<div align="center">

### 🌍 A professional-grade travel marketplace backend built with Django and Django REST Framework

*Manage property listings, user bookings, and reviews with enterprise-level architecture*

</div>

---

## 📋 Table of Contents

- [🚀 Key Features](#-key-features)
- [🛠 Tech Stack](#-tech-stack)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation & Setup](#️-installation--setup)
- [📖 API Documentation](#-api-documentation)
- [🧪 Custom Commands](#-custom-commands)
- [🛡️ Git & Security](#️-git--security)
- [📫 Contact](#-contact)

---

## 🚀 Key Features

<table>
  <tr>
    <td><b>🗄️ Relational Data Modeling</b></td>
    <td>Structured schema for <code>Listing</code>, <code>Booking</code>, and <code>Review</code> with UUID primary keys to ensure high security and non-sequential resource identification</td>
  </tr>
  <tr>
    <td><b>🌐 RESTful API</b></td>
    <td>Clean, resource-oriented endpoints for all core travel entities</td>
  </tr>
  <tr>
    <td><b>📚 Automated Documentation</b></td>
    <td>Fully interactive API exploration via Swagger UI and ReDoc</td>
  </tr>
  <tr>
    <td><b>🌱 Database Seeding</b></td>
    <td>Custom management command to instantly populate your environment with sample data (Mombasa, Nairobi, Nanyuki)</td>
  </tr>
  <tr>
    <td><b>📈 Scalability Ready</b></td>
    <td>Integrated with <code>django-environ</code> for secure configuration and configured for MySQL 8.0</td>
  </tr>
</table>

---

## 🛠 Tech Stack

<div align="center">

| Component | Technology |
|:---:|:---:|
| **Framework** | Django 5.x |
| **API Toolkit** | Django REST Framework |
| **Database** | MySQL 8.0 |
| **Documentation** | drf-yasg (OpenAPI 2.0) |
| **Task Queue** | Celery & RabbitMQ (Infrastructure Ready) |
| **Environment** | django-environ |

</div>

### Technologies Used

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white" />
  <img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white" />
  <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black" />
</p>

---

## 📂 Project Structure

```plaintext
alx_travel_app_0x00/
├── alx_travel_app/         # Core configuration
│   ├── settings.py         # App & DB settings
│   ├── urls.py             # Root URL routing (Swagger)
│   └── celery.py           # Celery application instance
├── listings/               # Core application logic
│   ├── management/         # Custom management commands (Seeder)
│   ├── models.py           # UUID-based Listing, Booking, and Review models
│   ├── serializers.py      # Data transformation logic
│   ├── urls.py             # App-level API routing
│   └── views.py            # API ViewSets
├── .env                    # Environment variables (Ignored by Git)
├── .gitignore              # Git exclusion rules
└── requirements.txt        # Dependency list
```

<details>
<summary><b>📁 Directory Breakdown</b></summary>
<br>

- **alx_travel_app/**: Core Django project configuration
  - `settings.py`: Application and database settings
  - `urls.py`: Root URL routing including Swagger documentation
  - `celery.py`: Celery application instance for async tasks

- **listings/**: Main application containing business logic
  - `management/`: Custom Django management commands
  - `models.py`: Database models with UUID primary keys
  - `serializers.py`: REST API data serialization
  - `urls.py`: Application-level URL routing
  - `views.py`: API ViewSets and endpoints

</details>

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8+
- MySQL 8.0
- Git

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/alx_travel_app_0x00.git
cd alx_travel_app_0x00
```

### 2️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True

# Database Settings
DB_NAME=alx_travel_app
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

> ⚠️ **Important:** Never commit your `.env` file to version control!

### 3️⃣ Setup Virtual Environment

**Windows:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Database Initialization & Seeding

```bash
# Create migrations
python manage.py makemigrations listings

# Apply migrations
python manage.py migrate

# Seed database with sample data
python manage.py seed
```

### 6️⃣ Run Development Server

```bash
python manage.py runserver
```

🎉 **Server running at:** `http://127.0.0.1:8000/`

---

## 📖 API Documentation

Once the server is running, access the interactive API documentation:

<div align="center">

| Documentation Type | URL | Description |
|:---|:---|:---|
| **Swagger UI** | [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) | Interactive API testing interface |
| **ReDoc** | [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) | Clean API documentation viewer |

</div>

### 🔗 Available Endpoints

<details>
<summary><b>View API Endpoints</b></summary>
<br>

**Listings:**
- `GET /api/listings/` - List all properties
- `POST /api/listings/` - Create new listing
- `GET /api/listings/{id}/` - Retrieve specific listing
- `PUT /api/listings/{id}/` - Update listing
- `DELETE /api/listings/{id}/` - Delete listing

**Bookings:**
- `GET /api/bookings/` - List all bookings
- `POST /api/bookings/` - Create new booking
- `GET /api/bookings/{id}/` - Retrieve specific booking
- `PUT /api/bookings/{id}/` - Update booking
- `DELETE /api/bookings/{id}/` - Delete booking

**Reviews:**
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create new review
- `GET /api/reviews/{id}/` - Retrieve specific review
- `PUT /api/reviews/{id}/` - Update review
- `DELETE /api/reviews/{id}/` - Delete review

</details>

---

## 🧪 Custom Commands

### Database Seeder

To reset or populate the database with sample travel listings (Mombasa, Nairobi, Nanyuki):

```bash
python manage.py seed
```

**What it does:**
- Clears existing data
- Creates sample listings with realistic travel destinations
- Populates sample bookings
- Generates sample reviews

<div align="center">
  <img src="https://img.shields.io/badge/Sample%20Data-Mombasa%20%7C%20Nairobi%20%7C%20Nanyuki-success?style=for-the-badge" />
</div>

---

## 🛡️ Git & Security

This project is configured with a `.gitignore` to prevent sensitive data from reaching version control.

### Verify Environment File is Ignored

```bash
git check-ignore -v .env
```

**Expected output:**
```
.gitignore:XX:.env    .env
```

### Security Best Practices

<table>
  <tr>
    <td>✅</td>
    <td><b>Environment Variables</b></td>
    <td>All sensitive data stored in <code>.env</code></td>
  </tr>
  <tr>
    <td>✅</td>
    <td><b>UUID Primary Keys</b></td>
    <td>Non-sequential, secure resource identification</td>
  </tr>
  <tr>
    <td>✅</td>
    <td><b>CORS Configuration</b></td>
    <td>Controlled cross-origin access</td>
  </tr>
  <tr>
    <td>✅</td>
    <td><b>Debug Mode</b></td>
    <td>Configurable via environment variables</td>
  </tr>
</table>

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is part of the ALX Software Engineering Program.

---

## 📫 Contact

<div align="center">

**Joel Mutiso** - Full Stack Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joelmutiso/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:joelwmutiso@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/joelmutiso)

</div>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,15,18&height=100&section=footer" />
</p>

<div align="center">
  <sub>Built with ❤️ by Joel Mutiso | ALX Software Engineering Program</sub>
</div>