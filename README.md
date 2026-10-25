# Django To-Do List Application

A task management web application built with Python, Django, SQLite/PostgreSQL, HTML, CSS and Bootstrap. Users can register, log in, and manage only their own tasks.

## Features

- User registration, login and logout
- Create, view, edit and delete tasks
- Mark tasks complete or incomplete
- Task title, description, due date and creation timestamp
- User-specific task access enforced on the server
- Form validation and Django messages
- Responsive Bootstrap interface
- SQLite for local development; PostgreSQL through `DATABASE_URL` in production
- WhiteNoise static-file serving for deployment

## Run locally (Windows)

1. Install Python 3.12 or newer from https://www.python.org/downloads/ and select **Add Python to PATH**.
2. Extract this project folder.
3. Open Command Prompt or PowerShell inside the `django_todo_resume_project` folder.
4. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`.

5. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Create the database tables and an admin user:

   ```powershell
   python manage.py migrate
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```powershell
   python manage.py runserver
   ```

8. Open http://127.0.0.1:8000/ in your browser. The admin panel is at http://127.0.0.1:8000/admin/.

## Deploy to Render

This repository includes `render.yaml` and `build.sh` for a Render Blueprint deployment.

1. Create a GitHub repository and push this project (steps below).
2. Sign in to https://render.com/ and connect your GitHub account.
3. Choose **New + → Blueprint**, select the repository, and let Render read `render.yaml`.
4. Approve creation of the web service and PostgreSQL database.
5. Wait for the build and deployment to finish, then open the `onrender.com` URL.
6. Test registration, login, task CRUD, and completion on the live site.

If Render asks for a Python version that is not available, change `PYTHON_VERSION` in `render.yaml` to a supported Python 3 version shown in Render's current documentation. Keep `DEBUG=False` in production. Do not commit real secrets or a production `.env` file.

**Free hosting caveat:** hosting and database free tiers, if available, can change and may sleep or have storage limits. Check the current Render plan details before deploying. For a public portfolio project, confirm the database persists across restarts.

## Push to GitHub

Create an empty repository on https://github.com/new (do not initialize it with a README if you are using this README). In a terminal opened in this project folder, run:

```bash
git init
git add .
git commit -m "Build Django To-Do List application"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the URL with your own repository URL. If Git is not installed, install it from https://git-scm.com/downloads.

## Suggested resume entry

**Django To-Do List Application | Python, Django, SQLite/PostgreSQL, Bootstrap**
- Built a task management web app with user authentication and task CRUD operations.
- Implemented user-specific task permissions, form validation, and task completion tracking.
- Configured production deployment with environment-based settings and PostgreSQL support.

Only include features, metrics, and a live deployment on your resume after you have tested them yourself.

## Before publishing

- [ ] Registration and login work
- [ ] One user cannot view or edit another user's tasks
- [ ] Add/edit/delete/complete task flows work
- [ ] No secret keys or passwords are committed
- [ ] README includes your actual live demo URL once deployed
- [ ] Replace `YOUR-USERNAME` in the Git commands
