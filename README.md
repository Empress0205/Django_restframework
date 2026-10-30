# Students & Employees API

A Django REST Framework API with token-based user registration, login and logout, plus CRUD endpoints for students and employees.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| POST | `/accounts/register/` | Create an account |
| POST | `/accounts/login/` | Log in |
| POST | `/accounts/logout/` | Log out |
| GET, POST | `/api/v1/students/` | List or create students |
| GET, PUT, DELETE | `/api/v1/students/<id>/` | Retrieve, update or delete a student |
| GET, POST | `/api/v1/employees/` | List or create employees |
| GET, PUT, DELETE | `/api/v1/employees/<id>/` | Retrieve, update or delete an employee |

## Stack

Python · Django 5.2 · Django REST Framework · SQLite

## Run locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Configuration

| Variable | Purpose | Default |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Django secret key — set a long random value outside local development | development-only key |
| `DJANGO_DEBUG` | `True` or `False` | `True` |
