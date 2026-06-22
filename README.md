This is a TaskManager project for my internship.

I followed the guidelines from the book "FastAPI - Modern Python Web Development" by Bill Lubanovic. Specifically I followed chapters 8, 9 and 10 to create a three-layer
backend architecture that involves an api layer (called as web layer in the book), a service layer for business logic/validations, and a db layer for writing to the database.

The database is made of two tables: A user table and a task table. 



TaskManager  
├── backend
│   ├── api
│   │   ├── __init__.py
│   │   └── routes
│   │       ├── health.py
│   │       ├── __init__.py
│   │       ├── tasks.py
│   │       └── users.py
│   ├── core
│   │   └── config.py
│   ├── db
│   │   ├── base.py
│   │   ├── models.py
│   │   └── session.py
│   ├── __init__.py
│   ├── main.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── task.py
│   │   └── user.py
│   └── services
│       ├── __init__.py
│       ├── task_service.py
│       └── user_service.py
├── client
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md
├── requirements.txt
└── uv.lock

