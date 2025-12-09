
````markdown
# Task Dashboard with Random Book Finder

This is a Django web application that allows users to manage tasks (CRUD operations) and also fetch random books from a public API. The dashboard shows task statistics with charts.

## Features

- Add, Update, Delete tasks
- Task status chart (Completed vs Pending)
- Fetch random books from Google Books API
- Responsive design using Bootstrap
- Fully functional API endpoints using Django REST Framework

## Tech Stack

- Backend: Django, Django REST Framework
- Frontend: HTML, Bootstrap, JavaScript
- Database: PostgreSQL
- Charts: Chart.js

## Installation & Setup

1. **Clone the repository**  
```bash
git clone <https://github.com/raja-1810/curd-app >
cd <your-project-folder>
````

2. **Create virtual environment**

```bash
python -m venv virtualenv
```

3. **Activate virtual environment**

* Windows:

```bash
virtualenv\Scripts\activate
```

* Mac/Linux:

```bash
source virtualenv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Configure Database**
   Update `settings.py` with your PostgreSQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'curdapp_db',
        'USER': 'curdapp_user',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

6. **Run migrations**

```bash
python manage.py migrate
```

7. **Run the development server**

```bash
python manage.py runserver
```

8. Open your browser at [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)

## API Endpoints

* `/api/tasks/` → List, Add, Update, Delete tasks (CRUD)
* `/api/external/books/` → Fetch books from Google Books API

## Author
* Raja Sahu

````