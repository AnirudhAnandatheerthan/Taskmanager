This is a TaskManager project for my internship.

I followed the guidelines from the book "FastAPI - Modern Python Web Development" by Bill Lubanovic. Specifically I followed chapters 8, 9 and 10 to create a three-layer
backend architecture that involves an api layer (called as web layer in the book), a service layer for business logic/validations, and a db layer for writing to the database. I also asked my dad for help with the structuring and debugging as well as AI.

The database is made of two tables: A user table and a task table. 



TaskManager  

.
├── backend
│ ├── api
│ │ ├── __init__.py
│ │ ├── __pycache__
│ │ └── routes
│ ├── core
│ │ ├── config.py
│ │ └── __pycache__
│ ├── db
│ │ ├── base.py
│ │ ├── models.py
│ │ ├── __pycache__
│ │ └── session.py
│ ├── __init__.py
│ ├── main.py
│ ├── __pycache__
│ │ └── __init__.cpython-312.pyc
│ ├── schemas
│ │ ├── __init__.py
│ │ ├── __pycache__
│ │ ├── task.py
│ │ └── user.py
│ └── services
│     ├── __init__.py
│     ├── __pycache__
│     ├── task_service.py
│     └── user_service.py
├── client
│ └── frontend
│     ├── babel.config.js
│     ├── jsconfig.json
│     ├── node_modules
│     ├── package.json
│     ├── package-lock.json
│     ├── public
│     ├── README.md
│     ├── src
│     └── vue.config.js
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md
├── requirements.txt
└── uv.lock

19 directories, 26 files
