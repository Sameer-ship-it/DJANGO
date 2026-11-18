# Django Student Records Demo

An educational Django project with templates and a SQLite-backed student-record workflow.

## Repository layout

```text
toy/
├── manage.py
├── toy/       # Django settings and URL configuration
└── store/     # Views, models, templates, and static assets
```

The app includes page views and student-related form/database examples. The repository also contains a local SQLite database and generated Python bytecode; use a fresh local database when setting up the project.

## Run locally

From the repository root:

```bash
git clone https://github.com/Sameer-ship-it/DJANGO.git
cd DJANGO/toy
python -m venv .venv
```

Activate the environment and install Django:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```

```bash
python -m pip install Django
python manage.py migrate
python manage.py runserver
```

Open the local address printed by Django. The project is configured for development; review the URL configuration and available templates for the routes in this example.

## Security and data

This code is for local learning. The current settings include development-only configuration, and the models include fields for passwords and identity data. Do not deploy this project publicly or enter real personal information without first implementing Django authentication, password hashing, secret management, input validation, and the deployment security checklist.

## Author

[Sameer Raza](https://github.com/Sameer-ship-it)
