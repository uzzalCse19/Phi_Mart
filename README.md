# Phimart - E-commerce API

Phimart is a RESTful e-commerce API built using Django REST Framework (DRF). It provides endpoints for managing products, categories, orders, and carts. The project also implements JWT authentication using Djoser and includes API documentation with Swagger.

## Features
- Product and category management
- Cart and order functionality
- JWT authentication using Djoser
- API documentation using Swagger (drf_yasg)

## Technologies Used
- **Django** - Backend framework
- **Django REST Framework (DRF)** - API development
- **Djoser** - Authentication
- **Simple JWT** - JWT authentication
- **drf-yasg** - API documentation (Swagger)
- **PostgreSQL** (or SQLite) - Database

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/uzzalCse19
   phimart.git
   cd phimart
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source phi_env/bin/activate  # On Windows use `.phi_env\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```    |

## API Documentation
Swagger documentation is available at:
```
http://127.0.0.1:8000/swagger/
```

## License
This project is licensed under the MIT License.

---
### Author
[Md.Uzzal](https://github.com/uzzalCse19)
#   P h i _ M a r t  
 