# PingPulse Backend

[![Django CI](https://github.com/your-username/pingpulse-django-vue/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/pingpulse-django-vue/actions/workflows/ci.yml)

This is the Django backend for PingPulse, a service for monitoring website uptime.

## Prerequisites

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/pingpulse-django-vue.git
    cd pingpulse-django-vue/backend
    ```

2.  **Create a `.env` file for development:**
    Create a file named `.env` in the `backend` directory and add the following environment variables. This file is for local development only and should not be used in production.

    ```
    SECRET_KEY=your-secret-key
    DJANGO_DEBUG=True
    DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
    DB_NAME=pingpulse_django
    DB_USER=pingpulse
    DB_PASSWORD=pingpulse
    DB_HOST=db
    DB_PORT=5432
    CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
    CELERY_BROKER_URL=redis://localhost:6379/0
    ```
    You can also use the `.env.example` file as a template.

## Running the Application

### Development

To run the application in a development environment, use the following command:

```bash
docker-compose up --build
```

This will start the Django development server and the PostgreSQL database. The application will be accessible at `http://localhost:8000`.

### Production Deployment

For production, a `docker-compose.prod.yml` file is provided which uses a production-grade WSGI server (Gunicorn) and does not mount the application code as a volume.

To deploy the application in production, use the following command, passing the environment variables directly:

```bash
SECRET_KEY=\'your-production-secret-key\' \
DJANGO_DEBUG=False \
DJANGO_ALLOWED_HOSTS=\'yourdomain.com,www.yourdomain.com\' \
DB_NAME=\'prod_db\' \
DB_USER=\'prod_user\' \
DB_PASSWORD=\'prod_password\' \
DB_HOST=\'db\' \
DB_PORT=\'5432\' \
CORS_ALLOWED_ORIGINS=\'https://yourdomain.com\' \
CELERY_BROKER_URL=\'redis://redis:6379/0\' \
docker-compose -f docker-compose.prod.yml up -d --build
```

**Important Notes for Production:**

*   **Environment Variables:** Do not use a `.env` file in production. Pass the environment variables directly to the `docker-compose` command as shown above, or use a secure secret management system.
*   **Database Backups:** Remember to implement a regular backup strategy for your PostgreSQL database.
*   **Logging:** For a robust production setup, consider implementing a centralized logging solution to collect and analyze logs from all services.

## Testing

This project uses `pytest` for testing. The tests are located in the `tests` directory of each application.

The tests are automatically run on every push and pull request to the `main` branch using GitHub Actions. You can see the status of the tests in the "Actions" tab of the GitHub repository.

To run the tests locally, you can use the following command:

```bash
pytest
```

## Demo User

A demo user is created automatically when the application is deployed. You can use the following credentials to log in:

*   **Email:** `demouser@example.com`
*   **Password:** `demopassword`

**Note:** User registration is disabled in this demo version. To re-enable it, uncomment the registration URL in `core/urls.py`.
