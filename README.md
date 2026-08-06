# Private Notes System

This project is a simple Django application for creating and managing personal notes. Notes are private by default but can be shared via a public URL.

## Features

- Log in and out
- Create, view, edit, and delete notes
- Viewing only notes owned by the logged in user
- Mark notes as public/private
- Share public notes without login
- Users cannot edit/delete notes they don't own

## Local Setup

1. Clone the repository:

```bash
git clone git@github.com:Xlentors/private-notes.git
cd private-notes
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
python -m pip install -r requirements.txt
```

4. Create the local SQLite database tables:

```bash
python manage.py migrate
```

5. Create a user:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/notes/` in your browser.

## Stack

- Python
- Django
- SQLite
- Django templates

## Running Tests

Activate the virtual environment, then run:

```bash
python manage.py test
```