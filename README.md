# api-quick-start

## Setup

Before you begin, ensure that Python 3.10 is installed on your system.

 Follow these steps to set up and run the API:

1. **Install Dependencies**: Open your terminal and run the following command to install all project dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Apply model changes to database schema**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. **Start the API**: To start the API, use the following command:

    ```bash
    python manage.py runserver
    ```

    This will launch the API, and you can access it at the provided URL.

## Customization Steps

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- change `blogs` or `posts` folder to the app name of your choice
- Search through entire code base for example `blog` , `blogs` to modify code to use your resource
  - `project/settings.py`
  - `project/urls.py`
  - App's files
    - `views.py`
    - `urls.py`
    - `admin.py`
    - `serializers.py`
    - `permissions.py`
  - "Front" files
    - if including a customer facing portion of the site then update/recreate:
      - `urls_front.py`
      - `views_front.py`
      - template files
      - Make sure to update project `urls.py` to add routes to the "front".
- Update blogModel with fields you need
  - Make sure to update other modules that would be affected by Model customizations. E.g. serializers, tests, etc.
- Rename `project/.env.sample` to `.env` and update as needed
  - To generate secret key use `python3 -c "import secrets; print(secrets.token_urlsafe())"`
- Run makemigrations and migrate commands when ready.
- Run `python manage.py collectstatic`
  - This repository includes static assets in repository. If you are using a Content Delivery Network then remove `staticfiles` from repository.
- Optional: Update `api_tester.py`

## Database

**NOTE:** If you are using Postgres instead of SQLite then make sure to install `psycopg2-binary` and include in `requirements.txt`
