# django-intro

## Setup

1. Create a virtual environment

    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment

    ```bash
    source venv/bin/activate
    ```
3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```
4. Create a django project

    ```bash
    django-admin startproject core .
    ```
5. Run the server

    ```bash
    python manage.py runserver
    ```
6. request the server

    ```bash
    curl http://localhost:8000/home/
    ```
7. request the server with a query parameter

    ```bash
    curl http://localhost:8000/home/?a=3&b=4
    ```
