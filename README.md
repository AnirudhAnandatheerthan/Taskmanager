# TaskManager - Basic Task management system
## A basic task management system that allows the creation, updation and deletion of tasks. Tasks can be assigned to users.


### About
This is a TaskManager project for my internship.

### Design
For the backend, I followed the guidelines from the book "FastAPI - Modern Python Web Development" by Bill Lubanovic. Specifically I followed chapters 8, 9 and 10 to create a three-layer
backend architecture that involves an api layer (called as web layer in the book), a service layer for business logic/validations, and a db layer for writing to the database. I also asked my dad for help with the structuring and debugging as well as AI.

The database is made of two tables: A user table and a task table. 

For the frontend, I followed some YouTube tutorials on Vue.js, as I found it easier to learn. If required, the frontend can be changed to use **react.js** instead of **Vue.js**

### Set Up Instructions

#### Pull the repository
The first step is to pull the repository into the local folder by using the command:
> **git pull https://github.com/AnirudhAnandatheerthan/Taskmanager.git**

This copies the entire folder structure locally, creating the backend and frontend directories.

#### Steps to run the backend
Command to run the docker and create a container (from the TaskManager directory)
> **docker compose up --build**


Command to open existing contatiners
> **docker compose up**


Command to stop the docker
> **docker compose down**

#### Steps to run the frontend
Installing Vue js to run the server
> **npm install -g @vue/cli**

To run the Vue js server, change directory to client->frontend and run the command
> **npm run serve**

#### Steps to test the project
1. Open your browser and copy/paste the URL from the previous steps
2. The task related endpoints are available at /api/v1/tasks
3. Since at the moment, there is no frontend for user creation, all users will have to be assigned to the predefined user 1, that is a dummy user - later I can enhance the project to allow for user maintenance
4. Enter some values for the task, assign to userID 1 and click **Submit** to create a new task



### Folder Structure for TaskManager  

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
