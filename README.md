# projet-integration-year2
2nd year integration project consisting in creating a web server, in communication with various services, including a JAVA simulator, and a robot that fetches.

Project created by Victor and Loïc. 

## 📁 Project Structure

```
Projet-integration-year2/
├── bot                     ── All references to the micropython robot 
    ├── ... (see "bot/README.md" for more informations)
├── python_controller       ── All references to the controller (made with python)
    ├── ... (see "python_controller/README.md" for more informations)
├── server                  ── All references to the web server (so the API)
    ├── ... (see "server/README.md" for more informations)
├── simulator               ── All references to JAVA simualtor
    ├── ... (see "simulator/README.md" for more informations)
├── web-frontend (useless)  ── All references to the IHM (deprecated, made with javascript / react)
    ├── ... (see "web-frontend/README.md" for more informations)
├── .gitignore              ── file to indicate github to ignore files
├── LICENSE                 ── License
├── README.md               ── Code documentation for the controller (made with python)
├── requirements.txt        ── All required librairies for the whole project
└── update-python-docs.bat  ── Home-made script to update all python docs 
```

## Install all required libraries for the whole project 

```bash
pip install -r requirements.txt
```

## Run server

```bash
cd server
uvicorn main:app --reload --env-file .env --host 0.0.0.0
```

## Generate/update all python docs (server / python_controller / bot) (on windows)

```bash
./update-python-docs.bat
```
