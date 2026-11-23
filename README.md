# Personal Contact Book

A web-based contact management application built with **Python and Django**. It allows users to manage their personal contacts through a simple interface, with authentication and user-level data protection.

This project was developed as part of my journey to learn backend and full-stack web development using Django.

## Overview

The Personal Contact Book provides a place to store, organize, search and manage personal contact information.



## Features

### Contact Management
- Create new contacts.
- View saved contacts.
- Update existing contact information.
- Delete contacts.
- Store contact details such as name, phone number, email and city.

### User Authentication
- User registration.
- User login and logout.
- Authenticated access to private contact pages.
- Session-based user authentication.

### Data Security
- Contacts are associated with their respective users.
- Users can access only their own contacts.
- Object-level ownership checks help prevent unauthorized access.
- CSRF protection for form submissions.

### Search and Navigation
- Search contacts.
- Filter contact records.
- Paginate contact listings.
- View individual contact details.
- Recently viewed contacts using Django sessions.

### User Experience
- Django templates and template inheritance.
- Reusable template components.
- Form validation and error handling.
- User feedback through Django's messages framework.
- Static files and CSS styling.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django | Backend web framework |
| SQLite | Relational database |
| Django ORM | Database operations |
| HTML5 | Page structure |
| CSS3 | Styling |
| Django Template Language | Dynamic page rendering |
| Git & GitHub | Version control and project hosting |

## Concepts Learned

This project helped me understand and apply the following concepts:

### 1. Django Fundamentals
- Django project and app structure.
- MVT architecture.
- URL routing and views.
- HTTP request-response lifecycle.
- Template rendering and context.
- Django Template Language.
- Static files and template inheritance.

### 2. Database and ORM
- Django models and database tables.
- Model fields and primary keys.
- Database migrations.
- Django ORM and QuerySets.
- Creating, retrieving, updating and deleting records.
- Relationships using ForeignKey.
- Database queries and filtering.

### 3. Forms and Validation
- HTML GET and POST requests.
- Django Forms and ModelForms.
- Form validation.
- `cleaned_data` and form errors.
- CSRF protection.

### 4. Authentication and Security
- Django's built-in User model.
- Registration, login and logout.
- Authentication vs authorization.
- Password hashing fundamentals.
- `login_required`.
- User-specific data access.
- Object ownership and IDOR prevention.

### 5. Django Features
- Messages framework.
- Pagination.
- Search and filtering.
- Sessions and cookies.
- Recently viewed records using sessions.

### 6. Testing
- Automated testing fundamentals.
- Django test framework.
- `TestCase`.
- Test client.
- Assertions.
- Model, form and view testing.
- Testing authentication and user ownership.

## Project Structure

```text
personal-contact-book/
│
├── manage.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── contacts/
    ├── migrations/
    ├── templates/
    │   └── contacts/
    ├── static/
    │   └── contacts/
    ├── tests/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    └── views.py
```

*The structure above represents the intended organization; actual files may vary depending on the final implementation.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/arshbhamra/Contact-Book.git
cd personal-contact-book
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

If a `requirements.txt` file is included:

```bash
pip install -r requirements.txt
```

Otherwise, install Django:

```bash
pip install django
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

### 8. Run tests

```bash
python manage.py test
```

## Learning Outcomes

Through this project, I moved beyond simply learning Django syntax and started understanding how different backend components work together.

I learned how to:

- Build a Django application from the ground up.
- Design models and interact with a relational database.
- Process user input through forms.
- Implement authentication and authorization.
- Protect user-specific data.
- Work with sessions, pagination and search.
- Understand and apply automated testing concepts.
- Organize a Django project into maintainable components.

## What's Next?

This project marks the completion of my first major Django learning milestone.

My next learning stages are:

1. Database design and Entity Relationship Diagrams.
2. Advanced Django ORM and query optimization.
3. Building a multi-user Blog application.
4. Intermediate Django architecture.
5. Django REST Framework.
6. React and full-stack application development.

The long-term goal is to become proficient in **Python/Django backend development and full-stack development using React**.

---

## Author

Learning and building with Python, Django and open-source technologies.

**Project:** Personal Contact Book  
**Category:** Backend Web Development  
**Framework:** Django  
**Status:** Completed — Learning Milestone 1